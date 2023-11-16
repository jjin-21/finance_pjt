from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        user = super().save_user(request, user, form, commit=False)
        data = form.cleaned_data
        user.nickname = data.get("nickname")
        user.age = data.get("age")
        user.gender = data.get("gender")
        user.asset = data.get("asset")
        user.salary = data.get("salary")
        if commit:
            user.save()
        return user
