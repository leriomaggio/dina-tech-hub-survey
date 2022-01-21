"""Questions and Choices in Survey"""

ROLES_QUESTION = "Qual è la tua occupazione?"
ROLES = (
    "Developer Frontend",
    "Developer Backend",
    "Developer Full-stack",
    "Manager (CTO, Tech Lead, Engineering Manager…)",
    "DevOps/sistemista/infrastruttura",
    "Sto studiando per diventare developer (informatica, ingegneria del software, computer science…)",
    "Other",
)

MOTIVATIONS_QUESTION = "Perché hai scelto di studiare/lavorare nel campo dell’informatica e della programmazione?"
MOTIVATIONS = (
    "perché mi piace e mi appassiona",
    "perché sono bravə a farlo",
    "perché penso porti ad un lavoro soddisfacente e remunerativo",
    "perchè è un campo dove si trova facilmente lavoro",
    "non saprei, era una scelta come un’altra",
)

AGE_RANGE_QUESTION = "Quanti anni hai ?"
AGE_RANGE = ("meno di 24", "25-35", "36-45", "più di 46")

GENDER_QUESTION = "Ti riconosci come...?"
GENDER = ("Uomo", "Donna")

COMPANY_SIZE_QUESTION = "Quanto è grande l'organizzazione in cui lavori (azienda, centro di ricerca, altro)?"
COMPANY_SIZE = (
    "non lavoro",
    "meno di 15 persone",
    "tra 16 e 50 persone",
    "+ di 51",
    "+ di 100",
)

COMPANY_TYPE_QUESTION = "L'azienda/organizzazione in cui lavori è"
COMPANY_TYPE = ("Non lavoro", "Italiana", "Multinazionale", "Other")

WOMEN_RATIO_QUESTION = "Quante donne lavorano come developer nella tua stessa azienda, o sono nel tuo stesso percorso di studi?"
WOMEN_RATIO = (
    "La maggioranza",
    "Circa la metà",
    "Meno della metà",
    "Nessuna",
    "Non so",
)

WOMEN_CIRCLE_QUESTION = "Oltre a quelle che lavorano/studiano con te, quante donne programmatrici/sistemiste/studentesse di informatica conosci?"
WOMEN_CIRCLE = ("Meno di 5", "Tra 6 e 15", "+ di 16")


WHY_GENDER_GAP_IN_IT_QUESTION = (
    "Secondo te, perché in informatica/programmazione le donne sono una minoranza?"
)

WHY_GENDER_GAP_IN_IT = (
    "non è vero che sono una minoranza",
    "perché in generale le donne interessate a informatica/programmazione sono una minoranza",
    "perché le donne non sono adatte a studiare informatica/programmazione",
    "perché occorre avere una mente razionale ed analitica",
    "perché questo ambiente (lavorativo e di studio) non è adatto alle donne",
    "perché è un lavoro impegnativo, anche come orari",
    "perché l’informatica è, ed è sempre stato, un campo maschile",
    "perché non è considerato normale che una donna studi scienze informatiche, ingegneria, e simili",
    "perché c'è un problema di mentalità per cui non si concepisce che la donna lavori in certi contesti",
    "perché è diffuso lo stereotipo che sia un lavoro da uomini",
    "perché non sono consapevoli delle loro capacità e pensano di non essere in grado",
    "nessuna delle precedenti",
)

SALARY_GAP_QUESTION = "Sai se il tuo compenso è diverso da quello delle altre persone che svolgono la tua stessa mansione?"
SALARY_GAP = (
    "non lo so",
    "non ho accesso ai dati, ma penso di guadagnare di più dei miei colleghi maschi, a parità di mansione",
    "non ho accesso ai dati, ma penso di guadagnare lo stesso dei miei colleghi maschi, a parità di mansione",
    "non ho accesso ai dati, ma penso di guadagnare meno dei miei colleghi maschi, a parità di mansione",
    "ho accesso ai dati, e so che guadagno di più dei miei colleghi maschi, a parità di mansione",
    "ho accesso ai dati, e so che guadagno lo stesso dei miei colleghi maschi, a parità di mansione",
    "ho accesso ai dati, e so che guadagno meno dei miei colleghi maschi, a parità di mansione",
)

# ------------------------------------------------------
# === Gender-Specialised Questions: W_ (Woman); M_ (Man)
# ------------------------------------------------------

# == Women Section
# ----------------
W_DISCRIMIATION_QUESTION = "Ti sei sentita discriminata, ostacolata, o messa in difficoltà nel tuo percorso di studi/carriera? Ti chiedo di pensare a situazioni, ostacoli e difficoltà che ti si presentano in particolare in quanto donna. "
W_DISCRIMINATION = (
    "no",
    "un po', ma facilmente superabile",
    "molto, ma nonostante tutto vado avanti",
    "talmente tanto che ho desistito o sto pensando di cambiare lavoro/carriera",
)

W_EXPERIENCE_QUESTION = "Hai mai vissuto situazioni come queste?"
W_EXPERIENCE = (
    "difficoltà di relazione con la maggioranza di colleghi maschi",
    "difficoltà di relazione con la maggioranza di colleghe donne",
    "sentirmi sola, diversa, esclusa nel gruppo di lavoro/studio",
    "mi sento invisibile, i colleghi maschi non mi considerano loro pari",
    "mi sento sottovalutata, non ascoltata, non vengo considerata brava abbastanza",
    "vengo apertamente sminuita, contraddetta",
    "situazioni fastidiose e imbarazzanti perché ci sono persone che mi trattano da inferiore e mi spiegano le cose con paternalismo",
    "clienti e colleghi chiedono consigli/specifiche tecniche ai colleghi maschi",
    "la famiglia e/o persone amiche mi sconsigliano/ostacolano nelle mie scelte di studio/lavoro",
    "mi sono sentita discriminata nel processo di recruiting (colloqui, inserimento lavorativo…)",
    "nessuna delle precedenti",
)

W_SUPPORT_QUESTION = "C’è qualcosa che pensi ti avrebbe potuto aiutare? Per esempio, 'sarebbe stato più facile se avessi saputo prima che...', o 'sarebbe stato più facile se ci fosse stata questa situazione...'"
W_SUPPORT = (
    "supporto da parte dei colleghi maschi",
    "supporto da parte delle colleghe donne",
    "supporto da parte di famiglia e persone amiche",
    "conoscere/lavorare con più donne che fanno il mio stesso lavoro",
    "conoscere modelli di 'donne che ce l’hanno fatta'",
    "se fare una certa scelta di studio/lavoro fosse stata considerata normale",
    "un ambiente scolastico aperto e attento all’interesse delle ragazze verso le materie STEM",
    "nessuna delle precedenti",
)

# == Men Section
# --------------
M_DISCRIMINATION_QUESTION = "Credi che le donne che fanno il tuo stesso lavoro/percorsi di studi, incontrino ostacoli, discriminazioni, situazioni di difficoltà? Ti chiedo di pensare a situazioni, ostacoli e difficoltà che si possono presentare in particolare alle donne in quanto tali."

M_DISCRIMINATION = (
    "no",
    "un po', ma facilmente superabili",
    "molto, ma nonostante tutto possono andare avanti",
    "talmente tanto che molte desistitono e cambiano lavoro/carriera",
)

M_EXPERIENCE_QUESTION = "Alle donne che lavorano nel tuo settore secondo te sono successe situazioni come quelle sotto (o magari le hai viste succedere tu stesso)?"

M_EXPERIENCE = (
    "difficoltà di relazione con la maggioranza di colleghi maschi",
    "difficoltà di relazione con la maggioranza di colleghe donne",
    "sentirsi sole, diverse, escluse nel gruppo di lavoro/studio",
    "sentirsi invisibili, i colleghi maschi non le considerano loro pari",
    "sentirsi sottovalutate, non ascoltate, non venire considerate abbastanza brave",
    "venire apertamente sminuite, contraddette",
    "situazioni fastidiose e imbarazzanti perché ci sono persone che le trattano da inferior e spiegano loro le cose con paternalismo",
    "clienti e colleghi chiedono consigli/specifiche tecniche solo e preferibilmente ai colleghi maschi",
    "la famiglia e/o persone amiche le sconsigliano/ostacolano nelle scelte di studio/lavoro",
    "sentirsi discriminate nel processo di recruiting (colloqui, inserimento lavorativo…)",
    "nessuna delle precedenti",
)

# -------------------------
# === Diversity Section ===
# -------------------------
INCREASE_GAP_QUESTION = (
    "Pensi che dovrebbero esserci più donne nel settore informatica/programmazione?"
)
INCREASE_GAP = ("Si", "No")

DIVERSITY_POLICY_QUESTION = "La tua azienda applica politiche di diversity & inclusion?"

DIVERSITY_POLICY = ("Non so cosa voglia dire", "Si", "No", "Non so")

WORKAROUND_GENDER_GAP_QUESTION = "Secondo te, cosa sarebbe utile fare, per favorire un aumento del numero di donne nel settore?"

WORKAROUND_GENDER_GAP = (
    "Non si può fare niente",
    "Applicare 'quote rosa' in fase di recruiting",
    "Cambiare la cultura aziendale",
    "Creare ambienti di lavoro più inclusivi",
    "Far conoscere storie e modelli di donne che lavorano in questo settore",
    "Diffondere e promuovere le materie STEM (Science, Technology, Engineering, Mathematics) nelle scuole",
    "Smontare gli stereotipi sul fatto che programmare sia un lavoro da uomini",
    "Denunciare le discriminazioni",
)