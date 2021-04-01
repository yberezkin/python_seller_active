# # encoding: utf-8
# class SellerActiveAPIException(Exception):
#     """
#     Generic Exception
#
#     Parameters:
#         message: str The error message
#         seller_active_code: str Amazon Error Code
#         error: list Amazon Error list
#
#     """
#     code = 999
#
#     def __init__(self, error):
#         try:
#             self.message = error[0].get('message')
#             self.seller_active_code = error[0].get('code')
#         except IndexError:
#             pass
#         self.error = error
