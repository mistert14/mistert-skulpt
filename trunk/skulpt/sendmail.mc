dnl # permettra de savoir que votre fichier de configuration a été modifié par vous
VERSIONID(`Installation Personnel')dnl
dnl # définir smtp.fournisseur.fr comme serveur de relais
define(`SMART_HOST',`smtp.fournisseur.fr')
dnl # demander au serveur de relayer le local
GENERICS_DOMAIN(localhost.localdomain localhost)dnl
dnl # demander au serveur d'utiliser une table de correspondance
FEATURE(`genericstable')dnl
dnl # masquer son adresse par l'adresse de free.fr
MASQUERADE_AS(`fournisseur.fr')dnl
dnl # masquer le header mais aussi l'enveloppe
FEATURE(masquerade_envelope)dnl
