# Etude de cas Arcane

### Installation

```
git clone https://github.com/azaracla/arcane-case-study.git
```
Pour créer l'environnement virtuel
```
python -m venv arcane-case-study/venv

cd arcane-case-study
```

Pour activer l'environnement virtuel et installer les dépendences.
```
source venv/bin/activate

pip install -r requirements.txt
```

### Utilisation
```
python run.py
```

### Informations

<p>Langage : Python</p>
<p>Framework : Flask</p>
<p>Base de donnée : SQLITE (avec l'ORM SQLAlchemy)</p>

### Description de l'API


| Méthode HTTP | URL                                | Action                                       |
|--------------|------------------------------------|----------------------------------------------|
| POST         | /register                          | Crée un nouvel utilisateur                   |
| PUT          | /account                           | Modifie ses données personnelles             |
| GET          | /account                           | Affiche ses données personnelles             |
| GET          | /assets                            | Affiche tous les biens immobiliers           |
| GET          | /assets/<ville>                    | Affiche tous les biens immobiliers par ville |
| POST         | /assets                            | Ajoute un nouveau bien                       |
| PUT          | /assets/<asset_id>                 | Modifie le bien identifié par <asset_id>     |
| GET          | /assets/<asset_id>/rooms           | Affiche toutes les pièces du bien <asset_id> |
| POST         | /assets/<asset_id>/rooms           | Ajoute une pièce au bien <asset_id>          |
| PUT          | /assets/<asset_id>/rooms/<room_id> | Modifie la pièce <room_id>                   |
| DELET        | /assets/<asset_id>/rooms/<room_id> | Supprime la pièce <room_id>                  |
| PUT          | /assets/<asset_id>                 | Modifie le bien <asset_id>                   |
| DELETE       | /assets/<asset_id>                 | Supprime le bien <asset_id>                  |

### Améliorations 

<p>Utiliser une base NoSQL comme MongoDB qui pourrait être bien appropriée au stockage de json </p>
<p>Utiliser Swagger pour la description de l'API</p>
