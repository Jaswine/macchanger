# Generated by Django 4.2.2 on 2023-06-21 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(default='', max_length=100, unique=True)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('ava', models.ImageField(blank=True, upload_to='avatars')),
                ('location', models.CharField(blank=True, max_length=164)),
                ('about', models.TextField(blank=True, max_length=500)),
                ('link_on_video', models.URLField(blank=True, max_length=1000)),
                ('background_color', models.CharField(default='#202020', max_length=10)),
                ('color', models.CharField(default='#ffffff', max_length=10)),
                ('card_background_color', models.CharField(default='transparent', max_length=20)),
                ('card_border_radius', models.CharField(default='10px', max_length=40)),
                ('card_box_shadow', models.CharField(default='1px 1px  20px 5px rgb(20,20,20, .4)', max_length=100)),
                ('card_border', models.CharField(default='1px solid rgb(20,20,20, .4)', max_length=40)),
                ('card_image_border_radius', models.CharField(default='1000px', max_length=40)),
                ('card_image_width', models.CharField(default='100px', max_length=10)),
                ('card_image_height', models.CharField(default='100px', max_length=10)),
                ('card_title_font_size', models.CharField(default='20px', max_length=40)),
                ('card_title_font_family', models.CharField(blank=True, default='', max_length=40)),
                ('card_title_font_color', models.CharField(blank=True, default='', max_length=40)),
                ('card_title_font_weight', models.CharField(default='bold', max_length=10)),
                ('card_text_font_size', models.CharField(default='18px', max_length=10)),
                ('card_text_font_family', models.CharField(blank=True, default='', max_length=30)),
                ('card_text_color', models.CharField(blank=True, max_length=20)),
                ('card_text_font_weight', models.CharField(blank=True, default='', max_length=10)),
                ('card_text_box_shadow', models.CharField(blank=True, default='', max_length=30)),
                ('card_text_border_bottom', models.CharField(blank=True, default='2px solid aliceblue', max_length=20)),
                ('card_text_border', models.CharField(blank=True, default='', max_length=20)),
                ('card_text_padding', models.CharField(blank=True, default='', max_length=20)),
                ('card_text_margin', models.CharField(blank=True, default='', max_length=20)),
                ('card_label_font_size', models.CharField(default='14px', max_length=10)),
                ('card_label_font_family', models.CharField(blank=True, max_length=30)),
                ('card_label_color', models.CharField(blank=True, max_length=20)),
                ('card_label_font_weight', models.CharField(default='400', max_length=5)),
                ('card_line_background_color', models.CharField(blank=True, default='white', max_length=20)),
                ('card_line_height', models.CharField(default='2px', max_length=10)),
                ('card_line_background', models.CharField(blank=True, default='', max_length=100)),
                ('card_line_border_radius', models.CharField(blank=True, default='10px', max_length=100)),
                ('card_button_background_color', models.CharField(default='white', max_length=20)),
                ('card_button_color', models.CharField(default='black', max_length=20)),
                ('card_button_border_radius', models.CharField(default='10px', max_length=20)),
                ('card_button_box_shadow', models.CharField(default='none', max_length=40)),
                ('card_button_background_color_hover', models.CharField(default='black', max_length=20)),
                ('card_button_color_hover', models.CharField(default='white', max_length=20)),
                ('card_button_border_radius_hover', models.CharField(blank=True, default='', max_length=20)),
                ('card_button_box_shadow_hover', models.CharField(default='none', max_length=40)),
                ('card_icon_color', models.CharField(blank=True, default='white', max_length=20)),
                ('font_icon_size', models.CharField(default='36px', max_length=20)),
                ('card_icon_color_hover', models.CharField(blank=True, default='', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CompanySocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=1000)),
                ('instagram', models.CharField(blank=True, max_length=1000)),
                ('youtube', models.CharField(blank=True, max_length=1000)),
                ('telegram', models.CharField(blank=True, max_length=1000)),
                ('twitter', models.CharField(blank=True, max_length=1000)),
                ('tiktok', models.CharField(blank=True, max_length=1000)),
                ('pinterest', models.CharField(blank=True, max_length=1000)),
                ('snapChat', models.CharField(blank=True, max_length=1000)),
                ('linkedin', models.CharField(blank=True, max_length=1000)),
                ('tumbler', models.CharField(blank=True, max_length=1000)),
                ('vk', models.CharField(blank=True, max_length=1000)),
                ('discord', models.CharField(blank=True, max_length=1000)),
                ('twitch', models.CharField(blank=True, max_length=1000)),
                ('quora', models.CharField(blank=True, max_length=1000)),
                ('whatsapp', models.CharField(blank=True, max_length=1000)),
                ('github', models.CharField(blank=True, max_length=1000)),
                ('sinaweibo', models.CharField(blank=True, max_length=1000)),
                ('viber', models.CharField(blank=True, max_length=1000)),
                ('skype', models.CharField(blank=True, max_length=1000)),
                ('soundCloud', models.CharField(blank=True, max_length=1000)),
                ('spotify', models.CharField(blank=True, max_length=1000)),
                ('their_website1', models.CharField(blank=True, max_length=1000)),
                ('their_website2', models.CharField(blank=True, max_length=1000)),
                ('their_website3', models.CharField(blank=True, max_length=1000)),
                ('yandex_taxi', models.CharField(blank=True, max_length=1000)),
                ('yandex_cards', models.CharField(blank=True, max_length=1000)),
                ('google_cards', models.CharField(blank=True, max_length=1000)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company')),
            ],
        ),
    ]