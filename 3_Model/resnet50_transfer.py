"""ResNet50 transfer-learning helpers for HeatmapCNNClassifier

Provides:
- create_resnet50_backbone(input_shape, weights='imagenet') -> base model (include_top=False)
- build_resnet50_classifier(base_model, n_classes, dropout=0.5) -> full model (base + custom top)
- compile_resnet50_model(model, learning_rate=1e-4)
- add_resnet50_methods_to_classifier(Class, freeze_base=True, weights='imagenet') -> attaches methods

Usage (in a notebook):

from 3_Model.resnet50_transfer import add_resnet50_methods_to_classifier
add_resnet50_methods_to_classifier(HeatmapCNNClassifier, freeze_base=True, weights='imagenet')

classifier = HeatmapCNNClassifier()
# ensure dataset-loading steps so classifier.n_classes exists
classifier.load_data_assignments()
classifier.load_heatmaps()
classifier.split_train_test()
classifier.scale_data()

input_shape = classifier.X_train_scaled.shape[1:]
base = classifier.create_resnet50_backbone(input_shape)
model = classifier.build_resnet50_classifier(base, classifier.n_classes)
model = classifier.compile_resnet50_model(model, learning_rate=1e-4)

"""

import tensorflow as tf
from tensorflow.keras import layers, Model


def create_resnet50_backbone(input_shape, weights='imagenet'):
    """Create ResNet50 backbone (include_top=False).

    input_shape: (H,W,C) — models expect C=3; if grayscale, duplicate channels beforehand.
    weights: 'imagenet' or None or path to weights file (Keras .h5)
    """
    # Validate input shape has 3 channels
    if len(input_shape) != 3:
        raise ValueError('input_shape must be (H, W, C)')

    # Use tf.keras.applications.ResNet50
    try:
        base = tf.keras.applications.ResNet50(
            include_top=False,
            weights=weights if weights in ('imagenet', None) else None,
            input_shape=input_shape,
            pooling=None,
        )
        # If a custom weights path was provided, try to load it
        if weights not in ('imagenet', None):
            try:
                base.load_weights(weights, by_name=True, skip_mismatch=True)
                print(f"Loaded ResNet50 weights from: {weights}")
            except Exception as e:
                print("Warning: could not load custom weights into ResNet50 backbone:", e)
    except Exception as e:
        raise RuntimeError(f"Failed to create ResNet50 backbone: {e}")

    return base


def build_resnet50_classifier(base_model, n_classes, dropout=0.5, dense_units=512):
    """Attach a small classification head to a ResNet50 backbone.

    base_model: Keras Model (include_top=False)
    n_classes: int
    """
    x = base_model.output
    x = layers.GlobalAveragePooling2D(name='gap')(x)
    x = layers.Dense(dense_units, activation='relu', name='fc1')(x)
    x = layers.BatchNormalization(name='bn_fc1')(x)
    x = layers.Dropout(dropout, name='dropout_fc1')(x)
    outputs = layers.Dense(n_classes, activation='softmax', name='predictions')(x)

    model = Model(inputs=base_model.input, outputs=outputs, name='resnet50_custom')
    return model


def compile_resnet50_model(model, learning_rate=1e-4):
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


def add_resnet50_methods_to_classifier(Class, freeze_base=True, weights='imagenet'):
    """Attach ResNet50 helper methods to a classifier class.

    Parameters:
        Class: classifier class (e.g., HeatmapCNNClassifier)
        freeze_base: if True, newly created backbone models will have their layers set non-trainable by default
        weights: 'imagenet' or None or path to custom weights (.h5). If custom path provided, function will
                 attempt to load it into the backbone.
    """

    def create_resnet50_backbone_method(self, input_shape, weights_local=weights):
        """Instance method wrapper to create a ResNet50 backbone."""
        base = create_resnet50_backbone(input_shape, weights=weights_local)
        if freeze_base:
            for layer in base.layers:
                layer.trainable = False
        return base

    def build_resnet50_classifier_method(self, base_model, n_classes=None, dropout=0.5, dense_units=512):
        n_classes = n_classes or getattr(self, 'n_classes', None)
        if n_classes is None:
            raise ValueError('n_classes is not set on classifier instance; run split_train_test() first')
        return build_resnet50_classifier(base_model, n_classes, dropout=dropout, dense_units=dense_units)

    def compile_resnet50_model_method(self, model, learning_rate=1e-4):
        return compile_resnet50_model(model, learning_rate=learning_rate)

    # Attach methods
    Class.create_resnet50_backbone = create_resnet50_backbone_method
    Class.build_resnet50_classifier = build_resnet50_classifier_method
    Class.compile_resnet50_model = compile_resnet50_model_method

    print(f"ResNet50 methods attached to {Class.__name__} (freeze_base={freeze_base}, weights={weights})")


# End of file
