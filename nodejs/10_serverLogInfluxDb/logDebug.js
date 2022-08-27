const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, printf } = format;
const logFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} - ${level}: ${message}`;
});
const logger = createLogger({
  format: combine(
    label({ label: 'ServerDebug' }),
    timestamp(),
    logFormat
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'debug.log' })
  ]
});

function WriteLogDebug(level, message){
    logger.log({
        level: level,
        message: message
      });
}

module.exports = WriteLogDebug;