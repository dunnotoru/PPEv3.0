from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, 
                            QComboBox, QPushButton, QSizePolicy)

class ModelPanel:
    def __init__(self, main_window):
        self.main_window = main_window
        self.panel = QWidget()
        self.model_combo = QComboBox()
        self.activate_model_btn = QPushButton("Активировать")
        self.manage_models_btn = QPushButton("Управление моделями")
        self.model_combo = None
        self.activate_btn = None
        self.manage_btn = None    
        self._setup_panel()
        
    def _setup_panel(self):
        layout = QHBoxLayout(self.panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        
        self.model_label = QLabel("Модель:   ")

        # Инициализация комбобокса
        self.model_combo = QComboBox()
        self.model_combo.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Fixed
        )
        
        # Инициализация кнопок с сохранением ссылок
        self.activate_model_btn.setEnabled(False)
        self.manage_models_btn.setEnabled(True)
        
        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combo, stretch=1)
        layout.addWidget(self.activate_model_btn)
        layout.addWidget(self.manage_models_btn)

        self.model_combo.currentTextChanged.connect(self._on_model_changed)
    
    def _on_model_changed(self):
        """Обработчик изменения модели"""
        self.activate_model_btn.setEnabled(True)
        if hasattr(self.main_window, 'control_panel'):
            self.main_window.control_panel.start_btn.setEnabled(False)