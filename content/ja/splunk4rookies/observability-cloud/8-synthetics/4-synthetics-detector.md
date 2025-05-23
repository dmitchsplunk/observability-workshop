---
title: 4. Synthetics Detector
weight: 4
---

これらのテストを 24 時間 365 日実行できるため、テストが失敗したり、合意した SLA よりも長く実行され始めた場合に、ソーシャルメディアやアップタイムウェブサイトから通知される前に、早期に警告を受けるための理想的なツールです。

![ソーシャルメディア](../images/social-media-post.png)

そのような事態を防ぐために、テストが 1.1 分以上かかっているかどうかを検知しましょう。

{{% notice title="演習" style="green" icon="running" %}}

- 左側のメニューから Synthetics ホームページに戻ります
- ワークショップのテストを再度選択し、ページ上部の{{% button style="white" %}} Create Detector {{% /button %}}ボタンをクリックします。  
  ![synth Detector](../images/synth-detector.png)
- **New Synthetics Detector**というテキスト（**1**）を編集し、`イニシャル -` [ワークショップ名]に置き換えます。
- {{% button %}}Run Duration{{% /button %}}と{{% button %}}Static threashold{{% /button %}}が選択されていることを確認します。
- **Trigger threasholt**（**2**）を`65,000`〜`68,000`に設定し、Enter キーを押してチャートを更新します。上図のように、しきい値ラインを切る複数のスパイクがあることを確認してください（実際のレイテンシーに合わせてしきい値を少し調整する必要があるかもしれません）。
- 残りはデフォルトのままにします。
- スパイクの下に赤と白の三角形の列が表示されるようになったことに注意してください（**3**）。赤い三角形は、テストが指定されたしきい値を超えたことを Detector が検出したことを知らせ、白い三角形は結果がしきい値を下回ったことを示します。各赤い三角形がアラートをトリガーします。
- アラートの重大度（**4**）は、ドロップダウンを別のレベルに変更することで変更できます。また、アラート方法も変更できます。**受信者を追加しないでください**。アラートストームの対象になる可能性があります！
- {{% button style="blue" %}}Actibate{{% /button %}}をクリックして、 Detector をデプロイします。
- 新しく作成した Detector を見るには、{{% button style="white" %}}Edit Test{{% /button %}}ボタンをクリックします。
- ページの下部にアクティブな Detector のリストがあります。

  ![Detectorのリスト](../images/detector-list.png)

- あなたの Detector が見つからず、*新しい Synthetics Detector*という名前のものが表示されている場合は、あなたの名前で正しく保存されていない可能性があります。*新しい Synthetics Detector*のリンクをクリックして、名前の変更をやり直してください。
- {{% button %}}閉じる{{% /button %}}ボタンをクリックして編集モードを終了します。
  {{% /notice %}}
