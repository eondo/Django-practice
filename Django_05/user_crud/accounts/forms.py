from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # model = User
        # # 이렇게 하면 될 수 있겠지만 django에서는 직접 참조하는 걸 권장하지 않음
        # # 현재 프로젝트에서 사용하는 user model을 반환해주는 함수를 제공
        fields = UserCreationForm.Meta.fields + ('email',) # 존재하는 필드 추가 가능

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)