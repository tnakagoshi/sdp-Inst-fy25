from django import forms

CATEGORY = (
    (None,'-----'),
    ('tool', '道具'),
    ('consumable', '消耗品'),
    ('other', 'その他')
)

SORT_CHOICES = (
    (None, '-----'),
    ('title', 'タイトル昇順'),
    ('-title', 'タイトル降順'),
    ('category', 'カテゴリ昇順'),
    ('-category', 'カテゴリ降順'),
)

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索キーワード',required=False)
    category = forms.ChoiceField(
        label='カテゴリー',
        choices=CATEGORY,
        required=False
    )
    sort_order = forms.ChoiceField(
        label='ソート順',
        choices=SORT_CHOICES,
        required=False
    )