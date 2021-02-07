# tap-copper

Author: Jacob Werderits (jacob@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:
- Generates a catalog of available data in Copper
- Extracts the following resources:
  - [Accounts](https://developer.copper.com/account-and-users/fetch-account-details.html)
  - [Users](https://developer.copper.com/account-and-users/list-users.html)
  - [Leads](https://developer.copper.com/leads/list-leads-search.html)
  - [People](https://developer.copper.com/people/list-people-search.html)
  - [Companies](https://developer.copper.com/companies/list-companies-search.html)
  - [Opportunities](https://developer.copper.com/opportunities/list-opportunities-search.html)
  - [Activities](https://developer.copper.com/activities/list-activities-search.html)
  - [Projects](https://developer.copper.com/projects/list-projects-search.html)
  - [Tasks](https://developer.copper.com/tasks/list-tasks-search.html)
  - [Custom Fields](https://developer.copper.com/custom-fields/general/list-custom-field-definitions.html)

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-copper.git
cd tap-copper
pip install -e .
```

2. Get an API key

Create a Copper [Authentication Token](https://developer.copper.com/?version=latest#authentication). Tokens are tied to a user's email (the user's permissions determine the data avaialable). After receiving an API token keep it somewhere safe, as you'll need it to authenticate requests. See "Create the config file" below for more information on using this API Token,

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your token and email

4. Run the application to generate a catalog.

```bash
tap-copper -c config.json --discover > catalog.json
```

5. Select the tables you'd like to replicate

Step 4 generates a a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

6. Run it!

```bash
tap-copper -c config.json --catalog catalog.json
```

### Resuming from a state file

```bash
tap-copper -c config.json --catalog catalog.json --state state.json
```

### Piping to Stitch

Create a stitch.config.json file:
```
{
  "client_id" : <your client_id int>,
  "token" : "<your token>",
  "small_batch_url": "https://<region>.stitchdata.com/v2/import/batch",
  "big_batch_url": "https://<region>.stitchdata.com/v2/import/batch",
  "batch_size_preferences": {}
}
```
Note that [region](https://www.stitchdata.com/docs/account-security/supported-data-pipeline-regions) is either `api.eu-central-1` or `us-east-1`.

Then run:
```bash
tap-copper -c config.json --catalog catalog.json | target-stitch --config stitch.config.json
```

Copyright &copy; 2019 Stitch
