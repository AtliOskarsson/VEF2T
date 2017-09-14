% include('template/header.tpl', title='{{ title }}')
<a href="{{ link1 }}">{{ linktext1 }}</a>
<a href="{{ link2 }}">{{ linktext2 }}</a>
<h1>{{ title }}</h1>
<p>{{ text }}</p>
<img src="{{ mynd }}">
% include('template/footer.tpl', info = '{{ contact }}')