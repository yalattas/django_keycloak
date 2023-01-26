# from boto3 import Session
# logger_session = Session(
#     aws_access_key_id='',
#     aws_secret_access_key='',
#     region_name='',
# )
# LOG_GROUP = env('LOG_GROUP')
# STREAM_NAME_INFO = env('STREAM_NAME_INFO')
# CLOUDWATCH_ENABLED = eval(env('CLOUDWATCH_ENABLED'))
# if CLOUDWATCH_ENABLED:
#     LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "aws": {
#             "format": (
#                 u"%(asctime)s [%(levelname)-8s] "
#                 "(%(module)s.%(funcName)s) %(message)s"
#             ),
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#     },
#     "handlers": {
#         "info_handler": {
#             "level": "INFO",
#             "class": "watchtower.CloudWatchLogHandler",
#             "boto3_session": logger_session,
#             "log_group": LOG_GROUP,
#             "stream_name": STREAM_NAME_INFO,
#             "formatter": "aws",
#         },
#     },
#     "loggers":{
#         "django":{
#             "level":"INFO",
#             "handlers": ["info_handler"],
#             "propagate": True,
#         },
#     },
# }
# # -----------------------------------------------------------------------
# # Xray configs ----------------------------------------------------------
# XRAY_ENABLED = eval(env('XRAY_ENABLED'))
# if XRAY_ENABLED:
#     tracing_name = env('XRAY_TRACING_NAME')
#     MIDDLEWARE.insert(0, 'aws_xray_sdk.ext.django.middleware.XRayMiddleware')
#     INSTALLED_APPS.append('aws_xray_sdk.ext.django')
#     XRAY_RECORDER = {
#         "AWS_XRAY_DAEMON_ADDRESS": "127.0.0.1:2000",
#         'AUTO_INSTRUMENT': True,
#         "AWS_XRAY_CONTEXT_MISSING": "LOG_ERROR",
#         # "PATCH_MODULES": ["requests"],
#         'AWS_XRAY_TRACING_NAME': tracing_name,
#         # 'DYNAMIC_NAMING': '*.munjiz.sa',
#         'PLUGINS': (),
#         'SAMPLING': True,
#     }