# Generated by Django 5.1.7 on 2025-03-15 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_comment_id_alter_post_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created"],
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-pub_date"],
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="posts.post",
                verbose_name="Пост",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(verbose_name="Текст комментария"),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="posts/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(verbose_name="Текст поста"),
        ),
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "following",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user", "following"), name="unique_follow"
                    )
                ],
            },
        ),
    ]
