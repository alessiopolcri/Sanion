# Sanion

## Descrizione
Sanion è un progetto focalizzato sulla sicurezza dei dispositivi. Fornisce strumenti per la gestione delle app installate, la ricerca e la pulizia delle tracce, e un "Panic Button" per l'eliminazione rapida di dati sensibili.

## Funzionalità

- **Gestione delle App**: Visualizza e gestisci le app installate sul tuo dispositivo.
- **Ricerca e Pulizia delle Tracce**: Trova e rimuovi tracce di dati che possono compromettere la tua privacy.
- **Panic Button**: Elimina rapidamente i dati sensibili in caso di emergenza.

## Struttura del Repository
- `.github/workflows/` - Configurazioni per l'integrazione continua.
- `data/xml/` - File XML necessari per l'analisi e il funzionamento.
- `lib/` - Librerie utilizzate nel progetto.
- `utils/` - Funzionalità di supporto.
- `cleaner.py` - Script per la pulizia dei dati.
- `config.json` - File di configurazione.
- `main.py` - Punto di ingresso principale dell'applicazione.
- `search.py` - Modulo per la ricerca di tracce nei dispositivi.
- `settings.json` - Impostazioni del progetto.

## Installazione

1. Clonare il repository:
   ```sh
   git clone https://github.com/alessiopolcri/sanion.git
   ```
2. Accedere alla directory del progetto:
   ```sh
   cd sanion
   ```
3. Installare le dipendenze richieste:
   ```sh
   pip install -r requirements.txt
   ```

## Utilizzo

Eseguire l'applicazione con:
```sh
python main.py
```

## Contribuire

Se desideri contribuire al progetto, segui questi passaggi:

1. Effettua un fork del repository.
2. Crea un nuovo branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Effettua le modifiche e confermale:
   ```sh
   git commit -m 'Aggiunta nuova funzionalità'
   ```
4. Effettua il push del branch:
   ```sh
   git push origin feature-branch
   ```
5. Apri una Pull Request.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per maggiori dettagli.

## Contatti

Per qualsiasi domanda o suggerimento, puoi contattarmi tramite il mio profilo GitHub.