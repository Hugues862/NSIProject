# Projet en NSI

Le projet est a l'image du jeux, Super Smash Bros de Nintendo

Le cahier des charges se trouve dans le Google Docs ainsi que d'autres informations importantes.

## Comment lancer le jeux
- Il faut commencer par aller dans le fichier "/HP/CLIENT/server.py"
  - modifiez la variable **server** avec son IPv4, (pour l'obtenir il faut aller dans le CMD, tapez:
  > ipconfig
  
    et récuperez l'IPv4
- Lancer le fichier **server.py** (de preference dans le cmd windows de facon a obtenir un affichage propre)
  - Commande pour lancer dans le CMD:
  > python "PATH/server.py"
- Modifier l'adresse du serveur de connection dans le fichier "/HP/CLIENT/classes/network.py"
  - Donc si vous le lancer en local, mettez le meme IPv4 que vous avez mis dans le fichier server.py.
- Lancer **deux fois** le fichier "client.py" de facon à avoir les deux clients. 
  **! Attention !** Il faut avoir les deux fenetres pygame des clients.





Lien Google Docs ==>  https://docs.google.com/document/d/1sox_KMu_VAwAoss42dzgaPiKh-DA4A_E_ce0RbX98gk/edit?ts=5f6c9028

Lien du Github ==> https://github.com/Hugues862/NSIProject/commits/master



Aides et liens pour les tutos:

https://www.techwithtim.net/tutorials/python-online-game-tutorial/client/
