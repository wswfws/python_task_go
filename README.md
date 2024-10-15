# GO game (chinese v.)
**Го** — азиатская настольная стратегическая игра. \
На разлинованной доске два игрока поочередно выставляют камни черного и белого цвета. \
**Цель игры** — обрести контроль над большей частью незанятых пересечений (территории), чем у противника.

### Китайский метод подсчета очков (китайские правила):
**Очки за территории и камни:** Игроки получают по одному очку за каждую пустую точку в пределах своей территории, а также по одному очку за каждый свой камень на доске. \
\
**Без учета пленников:** Захваченные камни не добавляются к счету (пленные камни не считаются отдельно). \
\
**Простота:** Это более прямой и интуитивный метод. Даже если пленных камней нет, счет идет за все камни и территории.

### Как работать с приложением
В приложении реализован **GUI** — графический интерфейс. При вызове программы откроется окно меню, в котором можно выбрать режим:
1) С противником-роботом;
2) Вдвоем за одним устройством.

### Для игры онлайн на сайте online-go.com
1) Регистрируемся
2) Берём sessionid из cookies
3) Ставим его и game_id в конфигурацию
4) Наслаждаемся

Также в начальном меню можно установить размер игровой сетки Го. Значение по умолчанию — 9. \
После выбора режима игра начнется автоматически. \
Первыми ходят черные. После выставления камня на поле ход переходит к белым и т. д.

В приложении также реализована возможность **спасовать**. При нажатии кнопки "пас" ход автоматически передается противнику, а счетчик пропустившего ход игрока прибавляется. \
После двух последовательных пасов обоих игроков игра прекращается. \
\
Каждый захваченный игроком камень противника также прибавляется к счёту противника. \
\
После окончания игры **в консоли** выводится **счёт** игроков в виде `(очки черных, очки белых)`. \
\
Авторы: \
Еценков Данил, Соколова Татьяна

