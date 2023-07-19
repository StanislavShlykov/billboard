'''
{% load spurl %}

{% if page_obj.has_previous %}
<a href="{% spurl query=request.GET set_query='page={{ 1 }}'%}">{{ 1 }}</a>
{% if page_obj.previous_page_number != 1 %}
...
<a href="{% spurl query=request.GET set_query='page={{ page_obj.previous_page_number }}'%}">{{ page_obj.previous_page_number }}</a>
{% endif %}
{% endif %}

{{ page_obj.number }}

{% if page_obj.has_next %}
<a href="{% spurl query=request.GET set_query='page={{ page_obj.next_page_number }}'%}">{{ page_obj.next_page_number }}</a>
{% if paginator.num_pages != page_obj.next_page_number %}
...
<a href="{% spurl query=request.GET set_query='page={{ page_obj.paginator.num_pages }}'%}">{{ page_obj.paginator.num_pages }}</a>
{% endif %}
{% endif %}



   {% if page_obj.has_previous %}
        <a class="page-link" href="{% spurl query=request.GET set_query='page=1'%}">1</a>
       {# <a href="?page=1">1</a>#}
       {% if page_obj.previous_page_number != 1 %}
           ...
           <a href="?page={{ page_obj.previous_page_number }}">{{ page_obj.previous_page_number }}</a>
       {% endif %}
   {% endif %}

   {# Информация о текущей странице #}
   {{ page_obj.number }}

   {# Информация о следующих страницах #}
   {% if page_obj.has_next %}
       <a href="?page={{ page_obj.next_page_number }}">{{ page_obj.next_page_number }}</a>
       {% if paginator.num_pages != page_obj.next_page_number %}
           ...
           <a href="?page={{ page_obj.paginator.num_pages }}">{{ page_obj.paginator.num_pages }}</a>
       {% endif %}
   {% endif %}

'''