class SQL:
  INIT_DB = """
    CREATE TABLE IF NOT EXISTS camera_models (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      comment TEXT
    );

    CREATE TABLE IF NOT EXISTS cameras (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      rtsp_source TEXT NOT NULL UNIQUE,
      comment TEXT,
      model_id INTEGER,
      FOREIGN KEY (model_id) REFERENCES camera_models(id) ON DELETE RESTRICT
    );

    CREATE INDEX IF NOT EXISTS idx_name ON camera_models(name);
    CREATE INDEX IF NOT EXISTS idx_rtsp_source ON cameras(rtsp_source);
    CREATE INDEX IF NOT EXISTS idx_model_id ON cameras(model_id);
  """