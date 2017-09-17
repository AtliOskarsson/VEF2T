% include('template/header.tpl', title= '{{ title }}')
<a href="{{ link1 }}">{{ linktext1 }}</a>
<a href="{{ link2 }}">{{ linktext2 }}</a>
<h1>{{ title }}</h1>
<img src="{{ gif }}">
% include('template/footer.tpl', info = '{{ contact }}')