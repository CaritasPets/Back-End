# Generated manually to fix foto_perfil field

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('users', '0005_remove_user_endereco_remove_user_tipo_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto_perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='uploader.image', verbose_name='Foto de Perfil'),
        ),
    ]