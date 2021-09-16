package ProjectsList;

public class Project{

    protected boolean isRemoved;
    protected String title;
    protected String description;
    protected String reasonForRemoval;
    protected String[] tags;
    protected String[] variations;
    protected String[] resources;

    public Project() {
    }

    public Project(String title) {
        this.title = title;
    }

    public boolean isRemoved() {
        return isRemoved;
    }

    public void setRemoved(boolean removed) {
        isRemoved = removed;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getReasonForRemoval() {
        return reasonForRemoval;
    }

    public void setReasonForRemoval(String reasonForRemoval) {
        this.reasonForRemoval = reasonForRemoval;
    }

    public String[] getTags() {
        return tags;
    }

    public void setTags(String[] tags) {
        this.tags = tags;
    }

    public String[] getVariations() {
        return variations;
    }

    public void setVariations(String[] variations) {
        this.variations = variations;
    }

    public String[] getResources() {
        return resources;
    }

    public void setResources(String[] resources) {
        this.resources = resources;
    }
}
