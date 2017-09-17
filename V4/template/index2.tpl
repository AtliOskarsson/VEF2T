% include('template/header.tpl', title='{{ title }}')
<a href="{{ link1 }}">{{ linktext1 }}</a>
<a href="{{ link2 }}">{{ linktext2 }}</a>
<h1>{{ title }}</h1>
<p><img src="{{ mynd1 }}"><img src="{{ mynd2 }}"><img src="{{ mynd3 }}"></p>
% include('template/footer.tpl', info = '{{ contact }}')