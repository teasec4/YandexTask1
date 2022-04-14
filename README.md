# YandexTask1
<h4>Задание 1</h4>  
Есть набор данных о стоимости недвижимости в Великобритании - .csv файл (скачать можно по ссылке
https://disk.yandex.ru/d/ZTnv3LiUeqEK5A, описание столбцов тут https://www.gov.uk/guidance/about-the-price-paid-data)
нужно написать программу, которая сформирует файл, в котором будет перечислена вся недвижимость, проданная больше 1-го раза.
Программа должна потреблять как можно меньше вычислительных ресурсов. Рассмотреть случаи экономии памяти и процессорного времени.

<h4>Описание фаилов</h4>

<ul>
  <li>
    <p>
      <b>createChunk.py</b>  -  оставляет только нужные столбцы и делит данные на чанки, для ускорения работы
    </p>
  </li>
   <li>
    <p>
      <b>main2.py</b> -  использует разработанный алгоритм, для решения задачи
    </p>
  </li>
  <li>
    <p>
      <b>merginAllData.py</b> -  объединяет чанки в один <b>.csv</b> фаил
    </p>
  </li>
  <li>
    <p>
      <b>nameOfColumns.txt</b> -  Шапка таблицы
    </p>
  </li>
   <li>
    <p>
      <b>test3.ipynb</b> -  Разработка и тестирование алгоритма
    </p>
  </li>
</ul>

<h4> Ход мыслей </h4>
<p> 
  Имеются данные (4,7 Гб)
</p>
<img src='https://user-images.githubusercontent.com/85108614/162947211-53f2dd02-c462-4b25-bdca-872d935e527f.png' />
<p>
  Это пример таблицы.
</p>
 По заданию нужно найти недвижимость, которая продавалась более 1 раза. Есть колонка <b>Price</b> - это когда-то сделанная разовая продажа. Предлагаю сдлеать "Уникальный адрес" из колонок <b>Street</b> + <b>PAON</b>(это номер дома) + <b>Country</b>, имея уникальынй адрес, можно по нему просуммировать продажи за всю историю существования недвижимости(по этому адресу). И затем сравнить с начальной таблицей по этому уникальному адресу, сравнивая мы будем две колонки <b>"Price_x"</b>  <b>"Price_y"</b>, если данные в этих колонках одинаковые, то <b>False</b>, разные - <b>True</b> , отсавляем только true значения, убираем дубликаты адресов, выводим результат.

