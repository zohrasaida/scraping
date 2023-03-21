
from fastapi.testclient import TestClient
import main
from main import app


client = TestClient(app)


def test_get_data():
    response = client.get("/page")
    assert response.status_code == 200

def test_get_data_content():
    response = client.get("/page/description")
    expected_output = {
  "page_description": {
    "description": "Ensit Junior Entreprise, créée en février 2013, est une organisation entrepreneuriale à but non lucratif intégrée au sein du réseau \"Junior Enterprises of Tunisia\".\n\nIntégralement générée par les étudiants ingénieurs de l’ENSIT, l'EJE réunit les compétences des meilleurs étudiants de l'école dans leurs différents domaines d'étude afin de garder sa stabilité et sa durabilité dans le réseau et sur le marché tunisien.\n\nNotre entité nous permet de mettre en pratique\nl'enseignement théorique que nous recevons et d'enrichir nos savoir-faire.",
    "emails": [
      "ensit.je@gmail.com"
    ],
    "about": "Association à but non lucratif",
    "fan_count": 5612,
    "engagement": {
      "count": 5612,
      "social_sentence": "5,6 K personnes aiment ça."
    },
    "picture": {
      "data": {
        "url": "https://scontent.ftun1-2.fna.fbcdn.net/v/t39.30808-1/306089529_5535611029823714_5876895488488061073_n.jpg?stp=cp0_dst-jpg_p50x50&_nc_cat=105&ccb=1-7&_nc_sid=dbb9e7&_nc_ohc=3q3s8a0R3f8AX_iW0vX&_nc_ht=scontent.ftun1-2.fna&edm=AJdBtusEAAAA&oh=00_AfA5Atde1-W2W7SD8tda3UumMsokYBQcNXUIIFJwB7ivGw&oe=641972FE"
      }
    },
    "has_whatsapp_number": false,
    "name": "Ensit Junior Entreprise",
    "id": "511313695586831"
  },
    }

    assert response == expected_output