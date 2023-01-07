@api_view(['GET', 'POST'])
def WebHook(request):
    if request.method == "GET":
        application_models.WebHook.objects.create(description=request.data)
        return JsonResponse(request.data)
    if request.method == "POST":
        application_models.WebHook.objects.create(description=request.data)
        # telegram_api_url = "https://api.telegram.org/bot5692281512:AAEGKUGJ32rCD2ka0uRpBcwOLXpDSNCpxEA"
        # chat_id = request.data['message']['chat']['id']
        # text = request.data['message']['text']
        # telegram_req = requests.get(
        #     telegram_api_url + f"/sendMessage?chat_id={chat_id}&text={text}"
        # )
        # print(telegram_req.json())
        if request.headers.get('content_type') == 'application/json':
            update = aiogram.types
            return JsonResponse(request.data)
    return JsonResponse({"message": "method not available"})


# {
#     'update_id': 409464431,
#     'message': {
#         'message_id': 333,
#         'from': {
#             'id': 1084153168,
#             'is_bot': False,
#             'first_name': 'Али',
#             'username': 'alikidiraliev',
#             'language_code': 'en'
#         },
#         'chat': {
#             'id': 1084153168,
#             'first_name': 'Али',
#             'username': 'alikidiraliev',
#             'type': 'private'
#         },
#         'date': 1673064733,
#         'text': 'test'
#     }
# }
