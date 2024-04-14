from flask import Flask
from src.routes.budget_routes import budget_routes
from src.database import get_db

app = Flask(__name__)
app.config['DATABASE'] = 'budget.db'

# Create SQLite database and table
def create_table():
    with app.app_context():
        db = get_db()
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS budget
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    amount REAL,
                    date DATETIME NOT NULL DEFAULT(datetime('now'))
                    )''')
        db.commit()

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.register_blueprint(budget_routes)

if __name__ == '__main__':
  app.run(debug=True)