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
      <b>createChunk.py</b>  -  делит данные на кусочки (достал маленький кусок данных для разработки алгоритма)
    </p>
  </li>
   <li>
    <p>
      <b>main.py</b> -  использует разработанный алгоритм, для создания итоговоых таблиц
    </p>
  </li>
  <li>
    <p>
      <b>merginData.py</b> -  объединяет таблиы созданные <b>main.py</b> в один  <b>.csv</b> фаил
    </p>
  </li>
  <li>
    <p>
      <b>nameOfColumns.txt</b> -  Шапка таблицы
    </p>
  </li>
   <li>
    <p>
      <b>test.ipynb</b> -  Разработка и тестирование алгоритма
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
 По заданию нужно найти недвижимость, которая продавалась более 1 раза. Есть колонка <b>Price</b> , но это когда-то сделанная разовая продажа. Предлагаю сдлеать "Уникальный адрес" из колонок <b>Street</b> + <b>PAON</b>(это номер дома) + <b>Locality</b>, имея уникальынй адрес, можно по нему просуммировать все продажи за всю историю существования недвижимости. И затем сравнить с полной таблицей, но по этому уникальному адресу, сравнивая мы будем удалять дубликаты, т.е если при сравнении по уникальному адресу, если попадаюстя два здания с одинаковой ценой и адресом, значит здание не продавалось более 1 раза, и затем эти дубликаты удаляем, оставляя только уникальные значения. 

