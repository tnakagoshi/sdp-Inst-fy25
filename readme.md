# しくみ

- 備品詳細に貸出ボタンを追加
  - CreateRentalViewとrental_form.htmlで貸出登録フォームを作る
  - 日付の項目を<input type="date">で入力されるため、モデルフォーム RentalModelFormを用意している
  - CreateRentalViewを呼び出すurls.pyではURLにパスパラメータを入れている（どの備品の貸し出しをするか、パスパラメータに渡すため）
- rental_form.htmlでは備品名は表示のみで入力にしないため、{{form.as_p}}の対象としていない（RentalModelFormには備品のIDは含めていない）
- CreateRentalViewのget_context_data()でパスパラメータに対応した備品データを取得しcontextに格納
- rental_form.htmlにhiddenフィールドを設定し、備品IDをパラメータとして渡るようにする
- CreateRentalViewのform_valid()でフォームからの送信を受けた際に、
  - 備品ＩＤをもとに備品データを取得してRentalモデルにセット
  - ログインユーザ情報をRentalモデルにセット
- success_urlはRentalViewにリダイレクトするようにreverse_lazyを使って指定
- RentalViewは動作確認用なので単純なListViewの挙動だけになっている