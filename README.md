# Description

Ceci est un projet backend d'API .
Ce projet est destiné a testé la version 1.1.6 du package elrahapi .
L'asynchrone a été testé en dernier , pour tester en mode synchrone reconfigurer le .env
puis retirer lazy="joined" des relationship.

## Installation

- **Avec Github :**
  ```bash
  git clone https://github.com/Harlequelrah/elrahapi-testproject-v-1.1.6
  ```

## Utilisation

- **Se rendre dans le repertoire du projet** :

```bash
  cd testproject
```

-  **Création d'un environnement virtuel :**
```bash
  python -m venv env
```
ou
```bash
  virtualenv env
```

-  **Installation des dépendances :**
```bash
  pip install -r requirements.txt
```

-  **Initialisation des variables d'environnement :**
```bash
  cp .env.test .env
```

-  **Initialisation d'alembic (Optionnel) :**
```python
  alembic init alembic
```


- **Lancement du serveur :**
```python
  elrahapi run
```

## `Technologies et bibliothèques`

- ElrahAPI
- Python
- Pydantic
- FASTAPI
- SQLAlchemy

## `Documentation`

- Models :

  - Post
  - Tag
  - Profile
  - User
  - Privilege
  - Role
  - UserRole
  - UserPrivilege
  - RolePrivilege

## `Captures de Swagger `

![Screenshot1](screenshots/screenshot_1.png)

![Screenshot2](screenshots/screenshot_2.png)

![Screenshot3](screenshots/screenshot_3.png)

![Screenshot4](screenshots/screenshot_4.png)

![Screenshot5](screenshots/screenshot_5.png)

![Screenshot6](screenshots/screenshot_6.png)

![Screenshot7](screenshots/screenshot_7.png)

![Screenshot8](screenshots/screenshot_8.png)

# Contact ou Support

Pour des questions ou du support, contactez-moi .

- **`Mail`** : **maximeatsoudegbovi@gmail.com**

- **`Telephone`** : **+228 91361029**
