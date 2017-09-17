% include('template/header.tpl', title= '{{ title }}')
<a href="{{ link }}">{{ linktext }}</a>
<h1>{{ title }}</h1>
<img src="{{ gif }}">
% include('template/footer.tpl', info = '{{ contact }}')