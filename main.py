import logger

# load config file
f = open("config.json", "r")
cfg = eval(f.read())
f.close()


l = logger.Logger(cfg["log_file"], cfg["fund_list"])
l.run(cfg["start_time"], cfg["gap"])
