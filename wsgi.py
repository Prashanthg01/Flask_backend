from reviewcruncher import app
# If logging app logging doesn't write to file in production include below code
import logging
logging.basicConfig(filename='AppEngine.log',level=logging.DEBUG)


if __name__ == '__main__':
	app.run()
