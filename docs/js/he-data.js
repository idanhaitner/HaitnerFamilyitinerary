/* Hebrew branding overlay — day content already Hebrew in data.js */
(function () {
  const HE = {
    trip: {
      title: "יפן 2026",
      subtitle: "הטיול של משפחת הייטנר",
      dates: "9–26 בספטמבר, 2026",
      notes: [
        "מסלול לפי אקסל המשפחה: טוקיו → האקונה → קיוטו → הירושימה → אוסקה → טוקיו.",
        "מלונות: Keio Plaza, Kajikaso, Musse Kyoto, Daiwa Roynet Hiroshima, Cross Osaka, Solaria Ginza.",
        "נחיתה בנריטה 17:40 (9/9); המראה מנריטה 22:30 (26/9).",
        "לחצו על מקומות לניווט במפות.",
      ],
    },
  };

  if (window.TRIP && HE.trip) {
    Object.assign(window.TRIP, HE.trip);
  }
})();
