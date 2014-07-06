from __future__ import absolute_import

from django.core.urlresolvers import reverse

from rest_framework import serializers

from .models import Document, DocumentVersion, DocumentPage


class ResourceDocumentPage(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentPage
        fields = ('url', 'content', 'page_label', 'page_number')


class ResourceDocumentVersion(serializers.HyperlinkedModelSerializer):
    pages = ResourceDocumentPage(many=True, read_only=True)

    class Meta:
        model = DocumentVersion
        fields = ('document', 'major', 'minor', 'micro', 'release_level', 'serial', 'timestamp', 'comment', 'file', 'mimetype', 'encoding', 'filename', 'checksum', 'pages')


class ResourceDocument(serializers.HyperlinkedModelSerializer):
    versions = ResourceDocumentVersion(many=True, read_only=True)

    class Meta:
        model = Document