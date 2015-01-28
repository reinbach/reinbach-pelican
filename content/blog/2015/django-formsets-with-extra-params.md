Title: Django - Passing extra params to Formsets
Date: 2015-01-28
Tags: django
Slug: django-formsets-with-extra-params
Author: Greg Reinbach

The scenario is that we want to use formsets on a model, but the model has a foreign key, and we only want a subset of the elements referenced by the foreign key.

i.e. We don't want all of the options returned by the foreign key to be shown.

I really like the Django class based views and use them as much as possible. I find that they make my life a lot easier. So when I needed to make use of some formsets in a particular view, but need the formsets to only display a subset of the elements referenced by the foreign key in the model, and tackled it in the following manner;

Here is our sample model, in this example when creating a transaction I only want to show those Accounts, referenced by account_debit / account_debit that are applicable / associated to the user making the request;

    #!python
    class Transaction(models.Model):
        account_debit = models.ForeignKey(Account, related_name="debit",
                                          verbose_name="debit")
        account_credit = models.ForeignKey(Account, related_name="credit",
                                           verbose_name="credit")
        amount = models.DecimalField(decimal_places=2, max_digits=8)
        summary = models.CharField(max_length=50)
        description = models.CharField(max_length=250, blank=True)
        date = models.DateField()


We create our normal model form, and the work happens in the `TransactionBaseFormSet`, we override `BaseFormSet` and in the `_construct` method we implement the logic that determines the account_debit/account_credit choices;

    #!python
    class TransactionForm(forms.ModelForm):
        class Meta:
            model = Transaction
            exclude = ["description"]


    class TransactionBaseFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop("user")
            super(TransactionBaseFormSet, self).__init__(*args, **kwargs)

        def _construct_form(self, i, **kwargs):
            form = super(TransactionBaseFormSet, self)._construct_form(i, **kwargs)
            account_choices = get_account_choices(self.user)
            form.fields["account_debit"].choices = account_choices
            form.fields["account_credit"].choices = account_choices
            form.fields["DELETE"].label = "Duplicate"
            return form


    TransactionFormSet = formset_factory(TransactionForm, can_delete=True, extra=0,
                                         formset=TransactionBaseFormSet)

And to get the user object into the formset we create a class based view normally and in the get_form_kwargs method we pass in the relevant user object we need/want;

    #!python
    class TransactionImportConfirmView(FormView):
        template_name = "import.html"
        form_class = TransactionFormSet
        success_url = reverse_lazy("accounts.transaction.list")

        def get_form_kwargs(self):
            kwargs = super(TransactionImportConfirmView, self).get_form_kwargs()
            kwargs["user"] = self.request.user
            return kwargs

And there we have it, we just had to really override the `BaseFormSet` and weave what magic we wanted in the `_construct` method and ensure we pass in any parameters we needed with the logic as we're all set.
