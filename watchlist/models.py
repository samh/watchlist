from django.db import models

WATCH_STATE_CHOICES = (
    ("N", "Not Started"),
    ("W", "Watching"),
    ("D", "Done"),
    ("L", "Deferred"), # L for later
    ("X", "Dropped"),
)

TYPE_CHOICES = (
    ("M", "Movie"),
    ("S", "Series"),
)

class Show(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # See also 'year' on AniDB (start date & end date)
    # TODO: pull data from AniDB (field for AniDB ID?)
    # This would be only for Anime...
    #anidb_id = models.CharField(max_length=20, null=True)
    
    # Relationships? (many-to-many to self, with relationship type attribute?)
    # With through model for relationship type (sequel, side story, ...).
    
    # Movie vs Series / OVA
    type = models.CharField(max_length=1, null=False, choices=TYPE_CHOICES)
    
    # Anime, animated, live-action
    
    # Group (Foreign key? Should be able to provide link.)
    encoding_group = models.CharField(max_length=20, blank=True)
    
    # Per-user things; probably need to be separate for multi-user app
    
    # Maybe watch state could be inferred from progress?
    # In-progress, maybe, but not done.
    # N or null?
    #watch_state = models.CharField(max_length=1, default="N", choices=WATCH_STATE_CHOICES)
    watch_state = models.CharField(max_length=1, null=True, blank=True,
        choices=WATCH_STATE_CHOICES)
    
    #done = BooleanField(default=False)
    
    # Free-form, but possibly with some Javascript for incrementing if
    # number-like (e.g. 2-07)?
    # Alternatively, could be season (optional) + episode, but there could
    # be special or weird episodes on occasion.
    # Hide if movie (I suppose it's possible I'd want to include a time
    # part way through a movie...)?
    progress = models.CharField(max_length=30, blank=True)
    
    #done_date = DateField(null=True)
    
    #rating = PositiveSmallIntegerField(null=True,
    #    validators=[
    #        MaxValueValidator(max_value=10), MinValueValidator(min_value=1)])
    note = models.TextField(blank=True)
    
    # Rewatch date(s)?
    # Complete history of progress changes?
    
    # Lists (many-to-many with list class?)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
