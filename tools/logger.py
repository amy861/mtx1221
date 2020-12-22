#导包 把日志模块和处理器一并导入
import logging.handlers

from lesson7_3.settings import DIR_NAME


class GetLogger:
    '''
    当已经创建了logger对象的时候，那么之后就不再创建了
    '''
    #把logger对象的初始值设置为None
    logger=None

    #创建logger对象，并且返回这个对象
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            # 2.设置日志级别（设置级别的时候用大写！后面调用的时候用小写）
            cls.logger.setLevel(logging.INFO)
            # 3.获取格式器
            # 3.1给格式器设置要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 3.2创建格式器，并且设置样式
            fm = logging.Formatter(fmt)
            # 4.创建处理器，按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename=DIR_NAME +'/logger/mtx.log',
                                                           when='H',  # 间隔多长时间把日志存放到文件中
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8'
                                                           )
            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)

        return cls.logger


if __name__ == '__main__':
    logger=GetLogger().get_logger()

    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('错误')
    logger.critical('致命')