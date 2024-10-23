from rest_framework import serializers
from .models import Category, Product, Tag
from ..utils import upload_image_to_cloudflare


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "image_url"]

    def create(self, validated_data):
        image = validated_data.pop("image", None)
        if image:
            image_url = upload_image_to_cloudflare(image)
            validated_data["image_url"] = image_url
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop("image", None)
        if image:
            image_url = upload_image_to_cloudflare(image)
            validated_data["image_url"] = image_url
        return super().update(instance, validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

