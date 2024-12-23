from django.urls import path, include
from counter.views import *
urlpatterns = [
    path("grace",login_view그레이스,name="login그레이스"),
    path("show_counter/grace", show_counter그레이스, name="show_counter그레이스"),
    path("increment_counter/grace", increment_counter그레이스, name="increment_counter그레이스"),
    path("done_counter/grace", done_counter그레이스, name="done_counter그레이스"),

    path("뉴턴", show_counter뉴턴, name="show_counter뉴턴"),
    path("increment_counter/뉴턴", increment_counter뉴턴, name="increment_counter뉴턴"),
    path("done_counter/뉴턴", done_counter뉴턴, name="5done_counter뉴턴"),

    path("늘품", show_counter늘품, name="show_counter늘품"),
    path("increment_counter/늘품", increment_counter늘품, name="increment_counter늘품"),
    path("done_counter/늘품", done_counter늘품, name="done_counter늘품"),

    path("데이터무제한", show_counter데이터무제한, name="show_counter데이터무제한"),
    path("increment_counter/데이터무제한", increment_counter데이터무제한, name="increment_counter데이터무제한"),
    path("done_counter/데이터무제한", done_counter데이터무제한, name="done_counter데이터무제한"),

    path("데카르트", show_counter데카르트, name="show_counter데카르트"),
    path("increment_counter/데카르트", increment_counter데카르트, name="increment_counter데카르트"),
    path("done_counter/데카르트", done_counter데카르트, name="done_counter데카르트"),

    path("도담", show_counter도담, name="show_counter도담"),
    path("increment_counter/도담", increment_counter도담, name="increment_counter도담"),
    path("done_counter/도담", done_counter도담, name="done_counter도담"),

    path("디세뇨", show_counter디세뇨, name="show_counter디세뇨"),
    path("increment_counter/디세뇨", increment_counter디세뇨, name="increment_counter디세뇨"),
    path("done_counter/디세뇨", done_counter디세뇨, name="done_counter디세뇨"),

    path("디아리오", show_counter디아리오, name="show_counter디아리오"),
    path("increment_counter/디아리오", increment_counter디아리오, name="increment_counter디아리오"),
    path("done_counter/디아리오", done_counter디아리오, name="done_counter디아리오"),

    path("라온제나", show_counter라온제나, name="show_counter라온제나"),
    path("increment_counter/라온제나", increment_counter라온제나, name="increment_counter라온제나"),
    path("done_counter/라온제나", done_counter라온제나, name="done_counter라온제나"),

    path("리사", show_counter리사, name="show_counter리사"),
    path("increment_counter/리사", increment_counter리사, name="increment_counter리사"),
    path("done_counter/리사", done_counter리사, name="done_counter리사"),

    path("매드매쓰", show_counter매드매쓰, name="show_counter매드매쓰"),
    path("increment_counter/매드매쓰", increment_counter매드매쓰, name="increment_counter매드매쓰"),
    path("done_counter/매드매쓰", done_counter매드매쓰, name="done_counter매드매쓰"),

    path("메이키스", show_counter메이키스, name="show_counter메이키스"),
    path("increment_counter/메이키스", increment_counter메이키스, name="increment_counter메이키스"),
    path("done_counter/메이키스", done_counter메이키스, name="done_counter메이키스"),

    path("빌리네어", show_counter빌리네어, name="show_counter빌리네어"),
    path("increment_counter/빌리네어", increment_counter빌리네어, name="increment_counter빌리네어"),
    path("done_counter/빌리네어", done_counter빌리네어, name="done_counter빌리네어"),

    path("세미콜론", show_counter세미콜론, name="show_counter세미콜론"),
    path("increment_counter/세미콜론", increment_counter세미콜론, name="increment_counter세미콜론"),
    path("done_counter/세미콜론", done_counter세미콜론, name="done_counter세미콜론"),

    path("소솜", show_counter소솜, name="show_counter소솜"),
    path("increment_counter/소솜", increment_counter소솜, name="increment_counter소솜"),
    path("done_counter/소솜", done_counter소솜, name="done_counter소솜"),

    path("수학에복종", show_counter수학에복종, name="show_counter수학에복종"),
    path("increment_counter/수학에복종", increment_counter수학에복종, name="increment_counter수학에복종"),
    path("done_counter/수학에복종", done_counter수학에복종, name="done_counter수학에복종"),

    path("실험의숲", show_counter실험의숲, name="show_counter실험의숲"),
    path("increment_counter/실험의숲", increment_counter실험의숲, name="increment_counter실험의숲"),
    path("done_counter/실험의숲", done_counter실험의숲, name="done_counter실험의숲"),

    path("심쿵", show_counter심쿵, name="show_counter심쿵"),
    path("increment_counter/심쿵", increment_counter심쿵, name="increment_counter심쿵"),
    path("done_counter/심쿵", done_counter심쿵, name="done_counter심쿵"),

    path("아리솔", show_counter아리솔, name="show_counter아리솔"),
    path("increment_counter/아리솔", increment_counter아리솔, name="increment_counter아리솔"),
    path("done_counter/아리솔", done_counter아리솔, name="done_counter아리솔"),

    path("아페토", show_counter아페토, name="show_counter아페토"),
    path("increment_counter/아페토", increment_counter아페토, name="increment_counter아페토"),
    path("done_counter/아페토", done_counter아페토, name="done_counter아페토"),

    path("에스쿱", show_counter에스쿱, name="show_counter에스쿱"),
    path("increment_counter/에스쿱", increment_counter에스쿱, name="increment_counter에스쿱"),
    path("done_counter/에스쿱", done_counter에스쿱, name="done_counter에스쿱"),

    path("에어로테크", show_counter에어로테크, name="show_counter에어로테크"),
    path("increment_counter/에어로테크", increment_counter에어로테크, name="increment_counter에어로테크"),
    path("done_counter/에어로테크", done_counter에어로테크, name="done_counter에어로테크"),

    path("엘리제", show_counter엘리제, name="show_counter엘리제"),
    path("increment_counter/엘리제", increment_counter엘리제, name="increment_counter엘리제"),
    path("done_counter/엘리제", done_counter엘리제, name="done_counter엘리제"),

    path("온에어", show_counter온에어, name="show_counter온에어"),
    path("increment_counter/온에어", increment_counter온에어, name="increment_counter온에어"),
    path("done_counter/온에어", done_counter온에어, name="done_counter온에어"),

    path("폴리머", show_counter폴리머, name="show_counter폴리머"),
    path("increment_counter/폴리머", increment_counter폴리머, name="increment_counter폴리머"),
    path("done_counter/폴리머", done_counter폴리머, name="done_counter폴리머"),

    path("피지카스트로", show_counter피지카스트로, name="show_counter피지카스트로"),
    path("increment_counter/피지카스트로", increment_counter피지카스트로, name="increment_counter피지카스트로"),
    path("done_counter/피지카스트로", done_counter피지카스트로, name="done_counter피지카스트로"),

    path("하람", show_counter하람, name="show_counter하람"),
    path("increment_counter/하람", increment_counter하람, name="increment_counter하람"),
    path("done_counter/하람", done_counter하람, name="done_counter하람"),

]

