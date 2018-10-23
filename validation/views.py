from django.http import HttpResponseRedirect
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import AnchoringResult, AuthorityResult, Company, Data, Useful


def anchoring(request, version):
    if version == 1:
        avg = 3
    elif version == 2:
        avg = 8.5
    else:
        version = 3
        avg = 0.0

    if request.POST:
        score = request.POST.get('score', None)

        if score:
            AnchoringResult.objects.create(
                version=avg,
                result=score,
            )
            return HttpResponseRedirect(reverse('thanks'))


    return render(request, 'anchoring/questionnaire.html', {
        'average': avg,
        'version': version,
    })


def authority(request, version):
    if version == 1:
        size = 2500
    elif version == 2:
        size = 5000000
    else:
        version = 3
        size = 0

    if request.POST:
        score = request.POST.get('score', None)

        if score:
            AuthorityResult.objects.create(
                version=size,
                result=score,
            )
            return HttpResponseRedirect(reverse('thanks'))


    return render(request, 'authority/questionnaire.html', {
        'size': size,
        'version': version,
    })


def rand_anchoring(request):
    results = AnchoringResult.objects.all()
    v1 = results.filter(version=3).count()
    v2 = results.filter(version=8.5).count()
    v3 = results.filter(version=0.0).count()

    counts = [v1, v2, v3]
    m = counts.index(min(counts))
    version = m+1

    return HttpResponseRedirect(reverse('anchoring', args=[version, ]))


def requirement(request, pk=None):
    if not pk or pk is 0:
        if pk is not 0:
            company = get_object_or_404(Company, name='overview')
            company.clicks = F('clicks') + 1
            company.save()

        return render(request, 'requirement/overview.html', {
            'companies': Company.objects.all().exclude(name='overview'),
        })

    company = get_object_or_404(Company, pk=pk)

    if request.POST:
        useful = request.POST.get('useful', None)

        if useful:
            useful = True if useful is 'y' else False
            Useful.objects.create(company=company, useful=useful)

        return HttpResponseRedirect(reverse('requirement', args=[0, ]))

    company.clicks = F('clicks') + 1
    company.save()

    return render(request, 'requirement/details.html', {
        'company': company,
        'datalist': Data.objects.filter(company=company),
    })


def thanks(request):
    return render(request, 'thanks.html', {})

