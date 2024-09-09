import unittest
from flask_testing import TestCase
from app import app, db, Task

class YourAppTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        # Utilisez une base de données de test
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()
        # Initialiser des données de test si nécessaire

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Testez la création d'une tâche
    def test_add_task(self):
        response = self.client.post('/add', data={'task': 'Nouvelle tâche de test'})
        self.assertEqual(response.status_code, 302)  # Vérifie que la redirection est correcte (vers la page d'accueil)
        
        # Assurez-vous que la tâche a été ajoutée à la base de données
        task = Task.query.first()
        self.assertIsNotNone(task)  # Vérifie que la tâche existe
        self.assertEqual(task.description, 'Nouvelle tâche de test')  # Vérifie que la description est correcte

    # Testez la suppression d'une tâche
    def test_delete_task(self):
        # Ajoutez une tâche pour pouvoir la supprimer
        test_task = Task(description="Tâche à supprimer")
        db.session.add(test_task)
        db.session.commit()

        # Supprimez la tâche
        response = self.client.post(f'/delete/{test_task.id}')
        self.assertEqual(response.status_code, 302)  # Vérifie la redirection après suppression

        # Assurez-vous que la tâche a été supprimée de la base de données
        deleted_task = Task.query.get(test_task.id)
        self.assertIsNone(deleted_task)  # Vérifie que la tâche n'existe plus

    # Testez l'affichage des tâches sur la page d'accueil
    def test_task_list_display(self):
        # Ajoutez des tâches de test à la base de données
        task1 = Task(description="Tâche 1")
        task2 = Task(description="Tâche 2")
        db.session.add_all([task1, task2])
        db.session.commit()

        response = self.client.get('/')
        self.assert200(response)  # Vérifie que la requête GET est réussie

        # Vérifiez que les tâches sont affichées sur la page
        self.assertIn('Tâche 1'.encode('utf-8'), response.data)  # Vérifie que "Tâche 1" est affichée
        self.assertIn('Tâche 2'.encode('utf-8'), response.data)  # Vérifie que "Tâche 2" est affichée

if __name__ == '__main__':
    unittest.main()

