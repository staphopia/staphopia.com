"""Viewsets related to Kmer tables."""
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.constants import KMER_TEST_SEQUENCE
from api.pagination import CustomReadOnlyModelViewSet
from api.queries.kmers import get_kmer_by_sequence, get_kmer_by_partition
from api.validators import validate_list_of_ids
from kmer.models import Total
from api.serializers.kmers import KmerTotalSerializer


class KmerViewSet(CustomReadOnlyModelViewSet):
    """A simple ViewSet for listing or retrieving Kmers."""

    queryset = Total.objects.all()
    serializer_class = KmerTotalSerializer

    @list_route(methods=['post'])
    def by_partition(self, request):
        """Given a parition, Kmers, samples IDs, return counts."""
        if request.method == 'POST':
            validator = validate_list_of_ids(request.data,
                                             max_query=50000)
            if validator['has_errors']:
                return Response({
                    "message": validator['message'],
                    "data": request.data
                })
            else:
                if validator['make_list']:
                    request.data['ids'] = [request.data['ids']]
                return self.formatted_response(get_kmer_by_partition(
                    request.data['extra']['partition'],
                    request.data['extra']['kmers'],
                    set(request.data['ids'])
                ), return_empty=True)

    @list_route(methods=['get'])
    def kmer_test(self, request, pk=None):
        import time
        start = time.time()
        results = get_kmer_by_sequence(KMER_TEST_SEQUENCE, [10173])
        time = '{0}ms'.format(
            int(
                (time.time() - start) * 1000.0
            )
        )
        return self.formatted_response(results, time=time)

    @list_route(methods=['get'])
    def partitions(self, request, pk=None):
        from kmer.partitions import PARTITIONS
        return Response(PARTITIONS)
