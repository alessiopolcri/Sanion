from lib.cli.cli import main
from lib.logger.logger import log
from lib.exceptions.exceptions import handle_exception
from utils.strings import STRINGS

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log(STRINGS['programma_interrotto'], level="WARNING")
    except Exception as e:
        handle_exception(e)