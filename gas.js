const SHEET_ID = "1G9x0wkYIfgKS1JW4tklR45UxAbuf60IF_EtZ857ekfg";

const sheet = SpreadsheetApp.openById(SHEET_ID);
const syllabusSheet = sheet.getSheetByName("waseda_zemi_syllabus");

const LastRow = sheet.getLastRow();

const changeRowHeight = () => {
  for (let i = 1; i < LastRow + 1; i++) {
    if (i % 2 === 1) {
      sheet.setRowHeight(i, 75);
      sheet.setColumnWidth(1, 300);
      sheet.setColumnWidth(2, 450);
      sheet.setColumnWidth(3, 450);
      sheet.setColumnWidth(4, 600);
      sheet.setColumnWidth(5, 1000);

      syllabusSheet
        .getRange(i, 3, 1, 3)
        .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
    } else {
      sheet;
    }
  }
};

const changeBackGroundColor = () => {
  let num = 1;

  for (let j = 1; j < LastRow + 1; j++) {
    if (4 * num - 3 === j) {
      syllabusSheet
        .getRange(j, 1, 1, 5)
        .applyRowBanding(SpreadsheetApp.BandingTheme.GREY);
      num++;
    }
  }
};
