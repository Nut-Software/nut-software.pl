const translations = {
  pl: {
    title: "Nut Software — oprogramowanie z pomysłem",
    description: "Nut Software — projektowanie i tworzenie oprogramowania dopasowanego do Twoich potrzeb.",
    skip: "Przejdź do treści",
    homeLabel: "Nut Software — strona główna",
    navLabel: "Nawigacja główna",
    navApproach: "Podejście",
    navContact: "Kontakt",
    eyebrow: "NUT SOFTWARE / POLSKA",
    heroTitle: "Dobry pomysł.<br /><em>Dobrze napisany kod.</em>",
    heroDescription: "Tworzymy oprogramowanie, które pomaga realizować konkretne cele. Prosto, uważnie i z myślą o tym, co będzie dalej.",
    heroCta: 'Porozmawiajmy o projekcie <span aria-hidden="true">↗</span>',
    heroMore: 'Poznaj nasze podejście <span aria-hidden="true">↓</span>',
    sectionLabel: "PODEJŚCIE",
    approachTitle: "Technologia ma sens,<br />kiedy <em>rozwiązuje problem.</em>",
    approachDescription: "Zaczynamy od zrozumienia celu. Następnie dobieramy rozwiązanie, które jest użyteczne dziś i daje przestrzeń do rozwoju jutro.",
    principleOneTitle: "Zrozumienie",
    principleOneText: "Najpierw słuchamy i porządkujemy potrzeby.",
    principleTwoTitle: "Prostota",
    principleTwoText: "Szukamy rozwiązań jasnych i wygodnych w użyciu.",
    principleThreeTitle: "Rozwój",
    principleThreeText: "Budujemy z myślą o kolejnych etapach produktu.",
    contactLabel: "KONTAKT",
    contactKicker: "MASZ POMYSŁ NA PROJEKT?",
    contactTitle: "Zacznijmy od <em>rozmowy.</em>",
    contactDescription: "Napisz kilka słów o tym, co chcesz zbudować. Odpowiemy i ustalimy kolejny krok.",
    footerLocation: "Polska · Tworzymy oprogramowanie z myślą o ludziach.",
    backToTop: "Wróć na górę ↑",
    switchLabel: "Switch to English"
  },
  en: {
    title: "Nut Software — thoughtful software",
    description: "Nut Software — thoughtful software designed around your goals.",
    skip: "Skip to content",
    homeLabel: "Nut Software — home",
    navLabel: "Main navigation",
    navApproach: "Approach",
    navContact: "Contact",
    eyebrow: "NUT SOFTWARE / POLAND",
    heroTitle: "A good idea.<br /><em>Thoughtful code.</em>",
    heroDescription: "We build software that helps turn clear goals into working products. Simply, thoughtfully, and with the future in mind.",
    heroCta: 'Let’s talk about your project <span aria-hidden="true">↗</span>',
    heroMore: 'Explore our approach <span aria-hidden="true">↓</span>',
    sectionLabel: "APPROACH",
    approachTitle: "Technology matters<br />when it <em>solves a problem.</em>",
    approachDescription: "We start by understanding the goal. Then we choose a solution that works today and leaves room to grow tomorrow.",
    principleOneTitle: "Understanding",
    principleOneText: "First, we listen and make sense of your needs.",
    principleTwoTitle: "Simplicity",
    principleTwoText: "We look for clear solutions that feel easy to use.",
    principleThreeTitle: "Growth",
    principleThreeText: "We build with the next stages of your product in mind.",
    contactLabel: "CONTACT",
    contactKicker: "HAVE A PROJECT IN MIND?",
    contactTitle: "Let’s start with <em>a conversation.</em>",
    contactDescription: "Tell us a little about what you want to build. We’ll reply and agree on the next step.",
    footerLocation: "Poland · Software built with people in mind.",
    backToTop: "Back to top ↑",
    switchLabel: "Przełącz na polski"
  }
};

function setLanguage(language) {
  const copy = translations[language];
  document.documentElement.lang = language;
  document.title = copy.title;
  document.querySelector('meta[name="description"]').content = copy.description;
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const value = copy[element.dataset.i18n];
    if (element.dataset.i18n === "heroCta" || element.dataset.i18n === "heroMore") {
      element.innerHTML = value;
    } else {
      element.textContent = value;
    }
  });
  document.querySelectorAll("[data-i18n-html]").forEach((element) => {
    element.innerHTML = copy[element.dataset.i18nHtml];
  });
  document.querySelectorAll("[data-i18n-aria]").forEach((element) => {
    element.setAttribute("aria-label", copy[element.dataset.i18nAria]);
  });
  const switcher = document.querySelector(".language-switch");
  document.querySelector(".button-primary").href = `mailto:sebastian.orzechowski.software@gmail.com?subject=${encodeURIComponent(language === "pl" ? "Nut Software — kontakt" : "Nut Software — enquiry")}`;
  switcher.textContent = language === "pl" ? "EN" : "PL";
  switcher.setAttribute("aria-label", copy.switchLabel);
  try { localStorage.setItem("nut-software-language", language); } catch (_) { /* Storage may be disabled. */ }
}

let savedLanguage;
try { savedLanguage = localStorage.getItem("nut-software-language"); } catch (_) { /* Storage may be disabled. */ }
setLanguage(savedLanguage === "pl" || savedLanguage === "en" ? savedLanguage : "pl");
document.querySelector(".language-switch").addEventListener("click", () => {
  setLanguage(document.documentElement.lang === "pl" ? "en" : "pl");
});
document.querySelector("#year").textContent = new Date().getFullYear();
