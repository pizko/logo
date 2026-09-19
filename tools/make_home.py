#!/usr/bin/env python3
"""Собирает src/index.html в стиле «пластилин».

Тексты, ссылки, телефоны, JSON-LD, Метрика и диалоги специалистов берутся из
исходной главной (orig/site/index.html → tools/head.html, tools/dialogs.html) без изменений.
Меняется только разметка секций под новый визуальный язык.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = ROOT / "tools"
head = (T / "head.html").read_text()
dialogs = (T / "dialogs.html").read_text()
sprite = (ROOT / "src/assets/clay/sprite.svg").read_text()

FONTS = ('  <link rel="preconnect" href="https://fonts.googleapis.com" />\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
         '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=Nunito:wght@900&display=swap" />\n'
         '  <link rel="stylesheet" href="assets/css/clay.css?v=2" />\n')
head = head.replace("</head>", FONTS + "</head>")


def obj(sym, cls, w=120, h=120, depth=None):
    d = f' data-depth="{depth}"' if depth else ""
    return f'<svg class="clay-obj {cls}" viewBox="0 0 {w} {h}" aria-hidden="true"{d}><use href="#{sym}"/></svg>'


TEL1, TEL1H = "tel:+79935947371", "+7 (993) 594‑73‑71"
TEL2, TEL2H = "tel:+79265947371", "+7 (926) 594‑73‑71"

NAV = [("#services", "Услуги"), ("#results", "Результаты"), ("#team", "Специалисты"), ("#school", "Подготовка к школе"),
       ("#prices", "Цены"), ("#reviews", "Отзывы"), ("novosti.html", "Новости"), ("#faq", "FAQ"), ("#contacts", "Контакты")]
nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)

body = f"""<body>
{sprite}
  <!-- HEADER -->
  <header class="site-header">
    <div class="container h-row clay-nav">
      <a class="brand" href="#top"><span class="logo" aria-hidden="true">★</span><span>Будущее</span></a>
      <nav class="hide-sm" aria-label="Разделы">{nav}</nav>
      <div class="actions hide-sm">
        <span class="header-phones"><a href="{TEL1}">{TEL1H}</a><a href="{TEL2}">{TEL2H}</a></span>
        <a class="btn btn-sm" href="#lead">Записаться</a>
      </div>
      <button class="burger show-sm" aria-expanded="false" aria-controls="mnav" id="burger" aria-label="Меню"><span></span><span></span></button>
    </div>
    <div class="mobile-nav" id="mnav">
      {nav}
      <a class="btn" href="#lead">Записаться</a>
      <a class="btn outline" href="{TEL1}">{TEL1H}</a>
      <a class="btn outline" href="{TEL2}">{TEL2H}</a>
    </div>
  </header>

  <!-- HERO -->
  <div id="top" class="hero">
    <div class="container">
      <div class="hero-slab clay-slab">
        <div class="hero-copy">
          <span class="eyebrow">Центр речи и развития в Раменском</span>
          <h1>Помогаем детям говорить свободно и уверенно</h1>
          <p class="lead">Диагностика, индивидуальные занятия и подготовка к школе. Бережно развиваем речь, внимание и уверенность ребёнка.</p>
          <div class="hero-benefits"><span class="hero-benefit">Без давления</span><span class="hero-benefit">Личная программа</span><span class="hero-benefit">Опытные специалисты</span><span class="hero-benefit">Очно и онлайн</span></div>
          <div class="hero-actions"><a class="btn btn-lg" href="#lead">Записаться на диагностику</a><a class="btn outline" href="#services">Посмотреть программы</a></div>
          <div class="hero-address"><span class="pin" aria-hidden="true"></span><span>г. Раменское, ул. Красноармейская, 13<br>Пн–Пт 9:00–20:00, Сб 10:00–17:00</span></div>
        </div>
        <div class="hero-visual" aria-label="Логопед и ребёнок играют с буквами">
          <div class="hero-plate"><img class="hero-image" src="assets/illustrations/hero-clay-v1.jpg" alt="Логопед и ребёнок занимаются с объёмными буквами" width="1200" height="957" fetchpriority="high" /></div>
          {obj("c-r", "h-r float-a", depth=".35")}
          {obj("c-a", "h-a float-b", depth=".25")}
          {obj("c-cube", "h-cube float-c", depth=".45")}
          {obj("c-star", "h-star float-b", depth=".3")}
          {obj("c-cloud", "h-cloud float-a", 140, 100, ".15")}
          {obj("c-bubble", "h-bubble float-c", 130, 120, ".4")}
        </div>
      </div>
    </div>
  </div>

  <section class="upcoming-event" id="upcoming-event" data-event-end="2026-09-07T00:00:00+03:00" aria-label="Ближайшее мероприятие">
    <div class="container"><div class="event-banner clay-card">
      <img src="assets/og/center-rechi-budushchee.jpg" alt="Центр речи «Будущее»" width="1200" height="630" />
      <div class="event-copy"><div class="muted">Ближайшее мероприятие</div><h2>Открытие Центра речи «Будущее»</h2><p><span class="event-time">6 сентября · 13:00</span> · г. Раменское, ул. Красноармейская, д. 13</p></div>
      <a class="btn" href="otkrytie-centra-rechi-budushchee.html">Подробнее</a>
    </div></div>
  </section>

  <section class="trust-strip" aria-label="Почему родители выбирают центр">
    <div class="container trust-islands">
      <div class="trust-island t1"><span class="token">1</span><div><strong>Первичная диагностика</strong><span>Бесплатно, 30 минут</span></div></div>
      <div class="trust-island t2"><span class="token">2</span><div><strong>Индивидуальный план</strong><span>Под возраст и задачи</span></div></div>
      <div class="trust-island t3"><span class="token">3</span><div><strong>Контроль прогресса</strong><span>Понятная динамика навыков</span></div></div>
      <div class="trust-island t4"><span class="token">4</span><div><strong>Помощь родителям</strong><span>Домашние рекомендации</span></div></div>
    </div>
  </section>

  <section class="audience-section" id="audience">
    <div class="container"><div class="muted">Для кого мы работаем</div><h2>Поддержка на каждом этапе развития</h2>
      <div class="audience-grid">
        <article class="audience-card a1">{obj("c-cube", "a-art")}<h3>Малыши</h3><p>Первые слова, запуск речи и общение без стресса.</p></article>
        <article class="audience-card a2">{obj("c-a", "a-art")}<h3>Дошкольники</h3><p>Звуки, словарный запас, внимание и готовность к школе.</p></article>
        <article class="audience-card a3">{obj("c-book", "a-art", 140, 110)}{obj("c-pencil", "a-art2", 140, 60)}<h3>Школьники</h3><p>Чтение, письмо, дисграфия, дислексия и учебная уверенность.</p></article>
        <article class="audience-card a4">{obj("c-bubble", "a-art", 130, 120)}<h3>Взрослые</h3><p>Дикция, публичная речь и восстановление после заболеваний.</p></article>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section id="services" class="services-section">
    <div class="blob blob-services" aria-hidden="true"></div>
    <div class="container">
      <div class="muted">Что мы делаем</div>
      <h2>Программы, которые решают конкретную задачу</h2>
      <p class="services-intro">Подберём формат работы с учётом задач ребёнка и подробно расскажем, как будет проходить программа.</p>
      <div class="services-showcase">
        <article class="service-tile s1">{obj("c-brain", "s-art", 130, 110)}<div class="token">01</div><h3>Компьютерная диагностика развития речи ребенка</h3><div class="service-meta"><span>от 60 до 90 минут</span></div><div class="service-price">3 000 ₽</div><a class="btn" href="#lead">Записаться</a></article>
        <article class="service-tile s2">{obj("c-puzzle", "s-art")}<div class="token">02</div><h3>Логопедический массаж индивидуальный</h3><div class="service-meta"><span>30 минут</span></div><div class="service-price">2 000 ₽</div><a class="btn" href="#lead">Записаться</a></article>
        <article class="service-tile s3">{obj("c-r", "s-art")}<div class="token">03</div><h3>Логопедическое занятие</h3><div class="service-meta"><span>30 минут</span></div><div class="service-price">2 500 ₽</div><a class="btn" href="#lead">Записаться</a></article>
        <article class="service-tile s4">{obj("c-123", "s-art", 200, 120)}<div class="token">04</div><h3>Курс из 8 занятий</h3><p>Логопедический массаж + коррекционные занятия</p><div class="service-price">28 000 ₽</div><a class="btn" href="#lead">Записаться</a></article>
      </div>
    </div>
  </section>

  <section class="process-section" id="process">
    <div class="container"><div class="muted">Как всё проходит</div><h2>Понятный путь от первой встречи к результату</h2>
      <div class="process-road">
        <svg class="cord" viewBox="0 0 600 60" preserveAspectRatio="none" aria-hidden="true"><use href="#c-cord"/></svg>
        <article class="process-step"><span class="step-num">1</span><h3>Знакомство</h3><p>Спокойно общаемся с ребёнком и родителем.</p></article>
        <article class="process-step"><span class="step-num">2</span><h3>Диагностика</h3><p>Определяем причины, сильные стороны и задачи.</p></article>
        <article class="process-step"><span class="step-num">3</span><h3>Личный план</h3><p>Согласуем цели, формат и ритм занятий.</p></article>
        <article class="process-step"><span class="step-num">4</span><h3>Занятия-игры</h3><p>Развиваем навыки без страха ошибки.</p></article>
        <article class="process-step"><span class="step-num">5</span><h3>Рекомендации</h3><p>Даём короткие и понятные упражнения домой.</p></article>
        <article class="process-step"><span class="step-num">6</span><h3>Контроль роста</h3><p>Отслеживаем динамику и корректируем маршрут.</p></article>
      </div>
    </div>
  </section>

  <!-- RESULTS -->
  <section id="results" class="results-section">
    <div class="container"><div class="results-slab clay-slab">
      <div class="muted">За что нас рекомендуют</div>
      <h2>Растёт не только речь — растёт уверенность</h2>
      <div class="results-orbit">
        <div class="result-cluster"><div class="result-pill"><strong>Измеримый прогресс</strong><p>Родитель понимает, что уже получается и над чем работаем дальше.</p></div><div class="result-pill"><strong>Игровые методики</strong><p>Ребёнок включается в задачу без давления и страха.</p></div><div class="result-pill"><strong>Вовлечение семьи</strong><p>Короткие упражнения легко встроить в обычный день.</p></div></div>
        <div class="speech-tree" aria-label="Дерево речевых навыков">
          <div class="tree-crown"></div><div class="tree-trunk"></div>
          {obj("c-a", "tree-letter a float-a")}{obj("c-r", "tree-letter b float-b")}{obj("c-ya", "tree-letter c float-c")}
          {obj("c-sun", "tree-sun float-b")}{obj("c-apple", "tree-apple float-a")}
        </div>
        <div class="result-cluster"><div class="result-pill"><strong>Комплексный взгляд</strong><p>Речь, дыхание, моторика, внимание и память работают вместе.</p></div><div class="result-pill"><strong>Бережное отношение</strong><p>Не ругаем за ошибки и не сравниваем детей между собой.</p></div><div class="result-pill"><strong>Личный план</strong><p>Темп, материалы и сложность заданий подбираем под ребёнка.</p></div></div>
      </div>
    </div></div>
  </section>

  <!-- TEAM -->
  <section id="team" class="team-section">
    <div class="container">
      <div class="muted">Кто вас ведёт</div>
      <h2>Наши специалисты</h2>
      <p class="team-intro">Нажмите на карточку, чтобы узнать об опыте и квалификации специалиста, а также посмотреть документы об образовании.</p>
      <p class="team-all"><a class="btn outline" href="specialisty.html">Все специалисты</a></p>
      <div class="specialists-grid">
        {''.join(f'''<button class="card specialist-card sp{i}" type="button" data-dialog="{slug}-dialog" aria-haspopup="dialog">
          <span class="sp-frame"><img class="specialist-photo" src="assets/specialists/{img}" alt="{name}" loading="lazy" width="{w}" height="{w}" /></span>
          {obj(deco, "sp-deco", *dims)}
          <span class="content"><h3>{name}</h3><span class="specialist-role">{role}</span><span class="specialist-more">Подробнее</span></span>
        </button>''' for i, (slug, img, name, role, w, deco, dims) in enumerate([
            ("vanyushkina", "vanyushkina.jpg", "Ванюшкина Светлана Ильинична", "Руководитель Центра речи «Будущее», логопед-дефектолог", 1254, "c-star", (120, 120)),
            ("akimova", "akimova.jpg", "Мария Александровна Акимова", "Психолог", 900, "c-smile", (120, 120)),
            ("kondrashov", "kondrashov.jpg", "Кондрашов Борис Алексеевич", "Специалист в области ЛФК и физической культуры и спорта", 900, "c-balls", (120, 80)),
            ("makarenko", "makarenko.jpg", "Марианна Александровна Макаренко", "Администратор Центра речи «Будущее»", 900, "c-bubble", (130, 120)),
            ("sidorova", "sidorova.jpg", "Ольга Николаевна Сидорова", "Педагог по математике и подготовке к школе", 900, "c-123", (200, 120)),
            ("mishenina", "mishenina.jpg", "Екатерина Мишенина", "Профориентолог подростков и взрослых, врач УЗ‑диагностики", 900, "c-puzzle", (120, 120)),
        ]))}
      </div>
    </div>
  </section>

{dialogs.replace('sidorova.jpg?v=20260804', 'sidorova.jpg')}
  <!-- SCHOOL PREPARATION -->
  <section id="school" class="school-section">
    <div class="blob blob-school" aria-hidden="true"></div>
    <div class="container">
      <div class="muted">Набор на 2026–2027 учебный год</div>
      <h2>Первый класс начинается задолго до 1 сентября</h2>
      <p class="school-lead"><strong>Уважаемые родители!</strong> Открыт набор на программы подготовки к школе. Мы помогаем детям не просто научиться читать и считать, а полюбить учиться, развить мышление, внимание и память.</p>
      <div class="school-grid">
        <div class="card school-card c1"><div class="content">
          <h3>1. Подготовка в мини-группах</h3>
          <p>В группе до 6 человек. Это позволяет уделить внимание каждому ребёнку, увидеть его сильные стороны, помочь преодолеть трудности и создать комфортную атмосферу, в которой хочется учиться.</p>
          <ul class="program-list"><li>Математика</li><li>Обучение чтению</li><li>Фонетика</li><li>Окружающий мир</li><li>Логика</li><li>Развитие внимания, памяти и речи</li></ul>
          <div class="schedule">Занятия: вторник и четверг • Длительность: 1 час 20 минут</div>
        </div></div>
        <div class="card school-card c2"><div class="content">
          {obj("c-pencil", "sc-art", 140, 60)}
          <h3>2. Индивидуальные занятия</h3>
          <p>Кроме групповых, ведётся набор на индивидуальные занятия — если ребёнку необходим персональный подход или индивидуальный темп обучения.</p>
          {obj("c-book", "sc-book float-c", 140, 110)}
        </div></div>
        <div class="card school-card c3 school-wide"><div class="content">
          <h3>3. Подготовка в математические классы</h3>
          <p>Для поступления в профильные классы и уверенной работы с задачами повышенной сложности.</p>
          <ul class="program-list"><li>Математическое мышление</li><li>Нестандартные задачи</li><li>Логика и анализ</li><li>Вступительные испытания</li><li>Контрольные работы</li><li>Система Л. Г. Петерсон</li></ul>
        </div></div>
        <div class="card school-card c4 school-wide"><div class="content">
          <h3>4. Подготовка к школе для детей экспатов из стран СНГ</h3>
          <p>Программа для детей, для которых русский язык не является родным: речь, чтение, письмо, математика и уверенная адаптация к школе.</p>
          <p><a class="btn" href="podgotovka-k-shkole-dlya-detey-iz-sng.html">Подробнее</a></p>
        </div></div>
        <div class="school-cta school-wide clay-slab">
          <div><h3>Запись на занятия</h3><p>г. Раменское, ул. Красноармейская, 13 • Центр речи «Будущее»</p></div>
          <div class="school-phones"><a class="btn light" href="{TEL1}">+7 (993) 594-73-71</a><a class="btn light" href="{TEL2}">+7 (926) 594-73-71</a></div>
        </div>
      </div>
    </div>
  </section>

  <!-- PRICES -->
  <section id="prices" class="prices-section">
    <div class="container">
      <div class="muted">Прозрачно и удобно</div>
      <h2>Цены</h2>
      <div class="price-grid">
        <div class="card price-card p1"><div class="content"><h3>Компьютерная диагностика развития речи ребенка</h3><div class="price">3 000 ₽</div><ul class="clean"><li><span class="check">✔</span> От 60 до 90 минут</li></ul><div class="price-act"><a class="btn" href="#lead">Записаться</a></div></div></div>
        <div class="card price-card p2"><div class="content"><h3>Логопедический массаж индивидуальный</h3><div class="price">2 000 ₽</div><ul class="clean"><li><span class="check">✔</span> 30 минут</li></ul><div class="price-act"><a class="btn" href="#lead">Записаться</a></div></div></div>
        <div class="card price-card p3"><div class="content"><h3>Логопедическое занятие</h3><div class="price">2 500 ₽</div><ul class="clean"><li><span class="check">✔</span> 30 минут</li></ul><div class="price-act"><a class="btn" href="#lead">Записаться</a></div></div></div>
        <div class="card price-card p4"><div class="content"><h3>Курс из 8 занятий</h3><div class="price">28 000 ₽</div><ul class="clean"><li><span class="check">✔</span> Логопедический массаж + коррекционные занятия</li></ul><div class="price-act"><a class="btn" href="#lead">Записаться</a></div></div></div>
      </div>
    </div>
  </section>

  <!-- REVIEWS -->
  <section id="reviews" class="reviews-section">
    <div class="container">
      <div class="muted">Отзывы</div>
      <h2>Нас выбирают семьи</h2>
      <div class="reviews-grid">
        <div class="card review r1"><div class="content"><blockquote>«Уже через месяц сын стал чётче произносить шипящие. Домашние задания короткие и интересные!»</blockquote><div class="muted-text">— Екатерина</div></div></div>
        <div class="card review r2"><div class="content"><blockquote>«Перестала заикаться в стрессовых ситуациях, появилась уверенность в речи.»</blockquote><div class="muted-text">— Ольга</div></div></div>
        <div class="card review r3"><div class="content"><blockquote>«Индивидуальный подход и отчёт по прогрессу каждые 2 недели — супер!»</blockquote><div class="muted-text">— Алексей</div></div></div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section id="faq" class="faq-section">
    <div class="container">
      <div class="muted">Частые вопросы</div>
      <h2>FAQ</h2>
      <div class="faq-list">
        <details><summary>С какого возраста идти к логопеду?</summary><div class="faq-a">Уже в 2–3 года можно оценить развитие речи и при необходимости запустить речь. Не ждите «само пройдёт».</div></details>
        <details><summary>Сколько занятий потребуется?</summary><div class="faq-a">Базовые звуки — 6–12 встреч при регулярной практике дома. Сложные случаи требуют индивидуального плана.</div></details>
        <details><summary>Делаете ли онлайн‑занятия?</summary><div class="faq-a">Да, используем Zoom/Meet. Вы получаете материалы и рекомендации для домашней работы.</div></details>
      </div>
    </div>
  </section>

  <section class="final-cta">
    <div class="container"><div class="final-cta-box clay-slab">
      {obj("c-star", "f-star float-a")}{obj("c-rainbow", "f-rainbow float-b", 160, 100)}{obj("c-ya", "f-ya float-c")}
      <div><div class="muted">Мы поможем сориентироваться</div><h2>Не знаете, с какого специалиста начать?</h2><p>Оставьте заявку на диагностику. Мы познакомимся с ребёнком, ответим на вопросы и предложим подходящую программу.</p></div>
      <div class="final-actions"><a class="btn light btn-lg" href="#lead">Записаться</a></div>
    </div></div>
  </section>

  <!-- LEAD + CONTACTS -->
  <section id="lead" class="lead-section">
    <div class="container contacts-grid" id="contacts">
        <div class="card contact-summary"><div class="content">
          <div><div class="muted">Как нас найти</div><h2>Контакты центра</h2></div>
          <ul class="clean">
            <li><strong>Адрес:</strong> Московская область, г. Раменское, Красноармейская улица, 13</li>
            <li><strong>График:</strong> Пн–Пт 9:00–20:00, Сб 10:00–17:00</li>
          </ul>
          <div class="contact-phone-actions"><a class="btn" href="{TEL1}">Позвонить: {TEL1H}</a><a class="btn outline" href="{TEL2}">Позвонить: {TEL2H}</a></div>
        </div></div>
        <div class="map-clay">
          <div class="map-label">Центр речи «Будущее»<span>Раменское, Красноармейская улица, 13</span></div>
          <iframe title="Карта: Центр речи «Будущее»" src="https://yandex.ru/map-widget/v1/?ll=38.234221%2C55.572609&z=17&mode=search&text=%D0%A6%D0%B5%D0%BD%D1%82%D1%80%20%D1%80%D0%B5%D1%87%D0%B8%20%C2%AB%D0%91%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B5%C2%BB%2C%20%D0%A0%D0%B0%D0%BC%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B5%2C%20%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B0%D1%80%D0%BC%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%2013&pt=38.234221%2C55.572609%2Cpm2rdm" loading="lazy" allowfullscreen></iframe>
        </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container footer-row">
      <div>© <span id="y"></span> Логопедический центр «Будущее»</div>
      <div class="footer-links">
        <a href="#">Политика конфиденциальности</a>
        <a href="#">Пользовательское соглашение</a>
      </div>
    </div>
  </footer>

  <div class="mobile-sticky" aria-label="Быстрые действия"><a class="btn outline" href="#contacts">Позвонить</a><a class="btn" href="#lead">Записаться</a></div>

  <script>
    // год в футере
    document.getElementById('y').textContent = new Date().getFullYear();
    // Ближайшее мероприятие скрывается сразу после времени окончания по Москве.
    const upcomingEvent = document.getElementById('upcoming-event');
    if (upcomingEvent && Date.now() >= new Date(upcomingEvent.dataset.eventEnd).getTime()) upcomingEvent.hidden = true;
    // мобильное меню
    const burger = document.getElementById('burger');
    const mnav = document.getElementById('mnav');
    if (burger) {{
      burger.addEventListener('click', () => {{
        const open = document.body.classList.toggle('nav-open');
        burger.setAttribute('aria-expanded', String(open));
      }});
      if (mnav) mnav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{{
        document.body.classList.remove('nav-open');
        burger.setAttribute('aria-expanded','false');
      }}));
    }}
    // карточки специалистов
    document.querySelectorAll('[data-dialog]').forEach(card => {{
      card.addEventListener('click', () => {{
        const dialog = document.getElementById(card.dataset.dialog);
        if (dialog && typeof dialog.showModal === 'function') dialog.showModal();
      }});
    }});
    document.querySelectorAll('.specialist-dialog').forEach(dialog => {{
      const close = dialog.querySelector('.dialog-close');
      if (close) close.addEventListener('click', () => dialog.close());
      dialog.addEventListener('click', event => {{
        const rect = dialog.getBoundingClientRect();
        const outside = event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
        if (outside) dialog.close();
      }});
    }});
  </script>
  <script src="assets/js/clay.js?v=1" defer></script>
<script src="/assets/js/qmark.js" defer></script></body>
</html>
"""
(ROOT / "src/index.html").write_text(head + body)
print("src/index.html", len(head + body) // 1024, "KB")
