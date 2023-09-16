# status.py
# track 항목 만들기,
# start from content photo
# amenities 같이 track 코드짜기
# contents 같이 followlist 코드짜기

# django api guide -> django rest knox, simple jwt

# 수정 필요:
# graphql
# login with frontend
# 사진을 url로 하게 field 조정
# 다 봐야함 영상들
# request 만들기
"""    def post(self, request):
        if request.user.is_authenticated:
            serializer = Task_DaySerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():  # Start of atomic transaction block
                    task_day = serializer.save(user=request.user)
                    difficult_questions_pks = request.data.get(
                        "difficult_questions")
                    for difficult_question_pk in difficult_questions_pks:
                        difficult_question = Difficult_Question.objects.get(
                            pk=difficult_question_pk)
                        task_day.difficult_question.add(difficult_question)
                # End of atomic transaction block
                serializer = Task_DaySerializer(task_day)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)"""