class Logger:
    __instance = None
    count = 0  # Counter to keep track of log messages

    @staticmethod
    def getInstance():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log(self, message):
        Logger.count += 1
        print(f"{message} (Log count: {Logger.count})")


if __name__ == "__main__":
    logger = Logger.getInstance()
    logger.log("First log message.")

    another_logger = Logger.getInstance()
    another_logger.log("Second log message.")
