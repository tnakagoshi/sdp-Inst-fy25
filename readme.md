# やっていること

- Gチームで、レビュー評価の平均順にソートする外部設計があるため、そのための実装例となります
- URLは /supplies/sort
- viewはreview_sort_view関数です
- Supplies.objects.annotateでモデルオブジェクトに一時的に項目を追加できるようです
- そのためレビューの平均点はHTMLテンプレートでも参照することができます