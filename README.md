# Project_Victorina
Групповой проект по информатике
План такой:
1) При запуске программы появляется главное меню, с названием викторины, там можно выбрать цвет кнопок и фона, а также ввести имя пользователя
2) Затем вы выбираете уровень сложности, которых будет два: lite и hard:
lite:
Всего будет 5 вопросов, 4 из которых очень сложные. И 4 варинта ответов в виде кнопок. Суть в том, что нажать вы можете только на правильный ответ, поскольку остальные 3 будут убегать при приближении курсора пользователя. А вот пятый вопрос будет очень простым, но вы физически не сможете ответить на него верно, так как будет такая же механика убегания кнопок.
hard:
Всего будет 5 вопросов, 4 из которых очень сложные. Здесь будут задаваться вопросы, ответы на которые вы должны будете вводить в поле, но суть в том, что при вводе любого ответа, вводиться будет правильный и если ответ состоит из 5 букв, а вы уже ввели 6, то нажатие на 6 клавишу означает отправку ответа, который является правильным. Например, какой запасной полисахарид у грибов? - ответ гликоген. Но вы, допустим, подумали, что крахмал. И начинаете вводить букву п, а в поле вводится "г". Вы вводите букву р, а поле вводится "л". И так далее. То есть на какие клавиши вы бы не нажимали, все равно будет вводиться правильный ответ. А вот с пятым вопросом все наоборот, он будет простым, при ответе на него вы начнете вводить его, но вводится будет не он.

Стоит еще отметить, что будет появляться счетчик правильных ответов, а последний неправильный будет вычитать какое-то огромное число, ведь вопрос был простым, а ответ - неправильный.

3) Так как вы ответили на последний вопрос неправильно на любом из уровней сложности, то будет появляться окно с надписью "И вы называете себя физтехом?".
Распределение обязанностей:
На Максиме - hard(механика + сами вопросы)
На Иветте - lite(механика + сами вопросы)
На Алесе - входная страница, счетчик, выходная страница
